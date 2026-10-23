"""Backtest engine for the Swaggy C strategy.

Event flow (mirrors a cTrader cBot):
  OnBar(hour)      -> pending limit fills, stop and take-profit hits      (process_hour)
  OnBar(day close) -> break-even, trailing, time exits, order expiry      (on_day_close)
  End of week      -> weekly bias + new Fib ladder                        (on_week_close)

Prices are Dukascopy BID. Long entries need ASK <= limit (bid <= limit - spread);
short exits need ASK to reach the level (bid + spread). Stops add slippage.
Same-hour ambiguity is resolved conservatively: stop before take-profit, and an
order filled in an hour can be stopped in that same hour but not take profit in it.
"""
import bisect
import csv
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from strategy import Idea, Order, find_setup, known_pivots, make_views, weekly_bias

NY = ZoneInfo("America/New_York")

# Per-symbol trading specs. Spread = typical round-trip cost in price units.
SPECS = {
    "EURUSD": dict(spread=0.00008, pip=0.0001, contract=100000, step=0.025),
    "GBPUSD": dict(spread=0.00012, pip=0.0001, contract=100000, step=0.025),
    "AUDUSD": dict(spread=0.00010, pip=0.0001, contract=100000, step=0.025),
    "USDCAD": dict(spread=0.00015, pip=0.0001, contract=100000, step=0.025),
    "GBPAUD": dict(spread=0.00025, pip=0.0001, contract=100000, step=0.025),
    "USDJPY": dict(spread=0.010, pip=0.01, contract=100000, step=5.0),
    "GBPJPY": dict(spread=0.025, pip=0.01, contract=100000, step=5.0),
    "XAUUSD": dict(spread=0.35, pip=0.10, contract=100, step=100.0),
}
CONV_PAIR = {"JPY": ("USDJPY", True), "CAD": ("USDCAD", True), "AUD": ("AUDUSD", False),
             "GBP": ("GBPUSD", False), "EUR": ("EURUSD", False), "USD": (None, False)}
LOT_STEP = 0.01


def load_params(path, overrides=None):
    import yaml
    y = yaml.safe_load(open(path))
    g = lambda *k: _get(y, k)
    p = dict(
        risk_pct=g("risk", "risk_per_idea_pct", "default"),
        ladder_pct=g("entries", "ladder_levels_pct", "default"),
        ladder_share=[g("risk", "ladder_risk_split", "default")[k] for k in ("fib_38_2", "fib_50", "fib_61_8")],
        max_open_risk_pct=g("risk", "max_open_risk_pct", "default"),
        max_ideas_per_symbol=g("risk", "max_ideas_per_symbol", "default"),
        max_same_ccy_dir=g("risk", "max_ideas_same_currency_direction", "default"),
        symbols=g("instruments", "default"),
        bias_pivot_bars=g("bias", "weekly_swing_pivot_bars", "default"),
        use_weekly_ema=g("bias", "use_weekly_ema_filter", "default"),
        ema_fast=8, ema_slow=14,
        pivot_bars=g("swing_detection", "pivot_bars_each_side", "default"),
        min_impulse_atr=g("swing_detection", "min_impulse_atr_mult", "default"),
        atr_period=g("swing_detection", "atr_period", "default"),
        max_pending_days=g("entries", "max_pending_days", "default"),
        stop_pct=g("stop_loss", "level_pct", "default"),
        stop_buffer_atr=g("stop_loss", "buffer_atr", "default"),
        targets_pct=g("take_profit", "targets_pct", "default"),
        close_fractions=g("take_profit", "close_fractions", "default"),
        min_rr=g("take_profit", "min_reward_risk", "default"),
        mgmt_pivot_bars=g("management", "higher_low_pivot_bars", "default"),
        trail_buffer_atr=g("management", "trail_buffer_atr", "default"),
        max_hold_days=g("management", "max_hold_days", "default"),
        breakeven_mode="tp1_or_higher_low",   # tp1_or_higher_low | tp1_only | higher_low_only | never
        trail_mode="d1_structure",            # d1_structure | none
        slippage_pips=g("backtest_assumptions", "slippage_pips", "default"),
        commission_per_lot=g("backtest_assumptions", "commission_per_lot_round_turn", "default"),
        start_balance=g("backtest_assumptions", "start_balance"),
        start_date="2014-01-01",
    )
    p.update(overrides or {})
    return p


def _get(d, keys):
    for k in keys:
        d = d[k]
    return d


# ---------------------------------------------------------------- data

def trading_day(ts_utc):
    """Forex day closes 17:00 New York."""
    return (ts_utc.astimezone(NY) + timedelta(hours=7)).date()


class SymbolData:
    def __init__(self, sym, data_dir, p):
        self.sym = sym
        self.spec = SPECS[sym]
        d = {"date": [], "open": [], "high": [], "low": [], "close": []}
        with open(Path(data_dir) / "daily" / f"{sym}.csv") as f:
            for r in csv.DictReader(f):
                d["date"].append(date.fromisoformat(r["date"]))
                for k in ("open", "high", "low", "close"):
                    d[k].append(float(r[k]))
        self.dates = d["date"]
        self.day_index = {dt: i for i, dt in enumerate(self.dates)}
        # weekly bars from daily (ISO weeks)
        w = {"high": [], "low": [], "close": []}
        self.week_of_day = []
        last_key = None
        for i, dt in enumerate(self.dates):
            key = dt.isocalendar()[:2]
            if key != last_key:
                w["high"].append(d["high"][i]); w["low"].append(d["low"][i]); w["close"].append(d["close"][i])
                last_key = key
            else:
                w["high"][-1] = max(w["high"][-1], d["high"][i])
                w["low"][-1] = min(w["low"][-1], d["low"][i])
                w["close"][-1] = d["close"][i]
            self.week_of_day.append(len(w["close"]) - 1)
        self.views = make_views(d, w, p)
        self.close = d["close"]
        # hourly bars
        self.h_time, self.h_day, self.h_o, self.h_h, self.h_l, self.h_c = [], [], [], [], [], []
        with open(Path(data_dir) / "hourly" / f"{sym}.csv") as f:
            for r in csv.DictReader(f):
                ts = datetime.strptime(r["time_utc"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                day = self.day_index.get(trading_day(ts))
                if day is None:
                    continue
                self.h_time.append(ts); self.h_day.append(day)
                self.h_o.append(float(r["open"])); self.h_h.append(float(r["high"]))
                self.h_l.append(float(r["low"])); self.h_c.append(float(r["close"]))
        self.last_hour_of_day = {}
        for i, dy in enumerate(self.h_day):
            self.last_hour_of_day[dy] = i

    def is_week_end(self, day):
        return day == len(self.dates) - 1 or self.week_of_day[day + 1] != self.week_of_day[day]


# ---------------------------------------------------------------- engine

class Backtest:
    def __init__(self, data_dir, p):
        self.p = p
        need = set(p["symbols"])
        for s in p["symbols"]:
            for ccy in (s[:3], s[3:]):
                pair = CONV_PAIR.get(ccy, (None,))[0]
                if pair:
                    need.add(pair)
        self.data = {s: SymbolData(s, data_dir, p) for s in sorted(need) if (Path(data_dir) / "daily" / f"{s}.csv").exists()}
        missing = [s for s in p["symbols"] if s not in self.data]
        if missing:
            raise FileNotFoundError(f"no data for {missing}")
        self.balance = p["start_balance"]
        self.ideas = []
        self.active = []        # live ideas only (speed)
        self.used_b = set()
        self.equity = []        # (date, balance, equity)
        self.next_id = 1
        self.start = date.fromisoformat(p["start_date"])

    # ---- money
    def usd_per_quote(self, sym, dt):
        q = "USD" if sym == "XAUUSD" else sym[3:]
        pair, inv = CONV_PAIR[q]
        if pair is None:
            return 1.0
        sd = self.data[pair]
        i = bisect.bisect_right(sd.dates, dt) - 1
        px = sd.close[max(i, 0)]
        return 1.0 / px if inv else px

    def round_units(self, sym, units):
        c = SPECS[sym]["contract"]
        lots = int(units / c / LOT_STEP) * LOT_STEP
        return lots * c

    def open_risk_pct(self):
        return sum(i.risk_usd for i in self.ideas if i.live() and not i.breakeven) / self.balance * 100

    def ccy_count(self, ccy, sign):
        n = 0
        for i in self.ideas:
            if not i.live():
                continue
            base, quote = (i.symbol[:3], i.symbol[3:])
            if ccy == base and i.direction == sign or ccy == quote and i.direction == -sign:
                n += 1
        return n

    # ---- main loop
    def run(self):
        events = []
        for s, sd in self.data.items():
            if s not in self.p["symbols"]:
                continue
            for i, t in enumerate(sd.h_time):
                events.append((t, s, i))
        events.sort()
        last_day = None
        for t, s, hi in events:
            sd = self.data[s]
            day = sd.h_day[hi]
            if sd.dates[day] < self.start:
                continue
            for idea in [x for x in self.active if x.symbol == s]:
                self.process_hour(idea, sd, hi)
            if sd.last_hour_of_day.get(day) == hi:
                self.on_day_close(sd, day)
                if sd.is_week_end(day):
                    self.on_week_close(sd, day, t)
                self.active = [x for x in self.active if x.live()]
            cur = trading_day(t)
            if cur != last_day:
                if last_day is not None:
                    self.snapshot(last_day)
                last_day = cur
        if last_day:
            self.snapshot(last_day)
        for i in self.ideas:
            if i.status == "open":
                i.exit_reason = "end_of_data"
        return self

    def snapshot(self, dt):
        eq = self.balance
        for i in self.ideas:
            if i.status == "open" and i.units_open > 0:
                sd = self.data[i.symbol]
                k = bisect.bisect_right(sd.dates, dt) - 1
                px = i.direction * sd.close[max(k, 0)]
                eq += i.units_open * (px - i.avg_entry()) * self.usd_per_quote(i.symbol, dt)
        self.equity.append((dt, self.balance, eq))

    # ---- hourly: fills and exits
    def process_hour(self, idea, sd, hi):
        p, d = self.p, idea.direction
        if d == 1:
            o, h, l = sd.h_o[hi], sd.h_h[hi], sd.h_l[hi]
            e_adj, x_adj = sd.spec["spread"], 0.0
        else:
            o, h, l = -sd.h_o[hi], -sd.h_l[hi], -sd.h_h[hi]
            e_adj, x_adj = 0.0, sd.spec["spread"]
        slip = p["slippage_pips"] * sd.spec["pip"]
        t = sd.h_time[hi]
        day = sd.h_day[hi]

        # 1) exits on the existing position (stop first: conservative)
        if idea.units_open > 0:
            if l + x_adj <= idea.stop:
                px = min(idea.stop, o + x_adj) - slip
                self.close_units(idea, idea.units_open, px, t, "stop" if not idea.breakeven else "breakeven/trail")
                return
            for k, tp in enumerate(idea.tps):
                if idea.tp_hit[k] or idea.units_open <= 0:
                    continue
                if h - x_adj >= tp:
                    if k == 0:
                        idea.units_at_tp1 = idea.units_filled()
                        for od in idea.orders:
                            if not od.filled:
                                od.cancelled = True
                        if p["breakeven_mode"] in ("tp1_or_higher_low", "tp1_only"):
                            idea.stop = max(idea.stop, idea.avg_entry())
                            idea.breakeven = True
                    base = idea.units_at_tp1 or idea.units_filled()
                    qty = idea.units_open if k == len(idea.tps) - 1 else min(idea.units_open, self.round_units(idea.symbol, base * p["close_fractions"][k]))
                    idea.tp_hit[k] = True
                    idea.max_tp = k + 1
                    if qty > 0:
                        self.close_units(idea, qty, tp, t, f"tp{k + 1}")
                else:
                    break
            if idea.status == "closed":
                return

        # 2) new extreme beyond B before any fill: the setup is replaced
        if idea.status == "pending" and h > idea.b:
            idea.status, idea.exit_reason, idea.exit_time = "cancelled", "new_extreme_before_fill", str(t)
            return

        # 3) limit fills
        filled_now = False
        for od in idea.orders:
            if od.filled or od.cancelled or od.units <= 0:
                continue
            if l + e_adj <= od.price:
                od.filled, od.fill_price, od.fill_time = True, min(od.price, o + e_adj), str(t)
                idea.units_open += od.units
                filled_now = True
                if idea.first_fill_day < 0:
                    idea.first_fill_day = day
                    idea.status = "open"
        if filled_now and l + x_adj <= idea.stop:
            self.close_units(idea, idea.units_open, idea.stop - slip, t, "stop")

    def close_units(self, idea, qty, px, t, reason):
        sym = idea.symbol
        dt = trading_day(t) if isinstance(t, datetime) else t
        conv = self.usd_per_quote(sym, dt)
        pnl = qty * (px - idea.avg_entry()) * conv
        comm = qty / SPECS[sym]["contract"] * self.p["commission_per_lot"]
        idea.units_open -= qty
        idea.pnl_usd += pnl - comm
        idea.costs_usd += comm
        self.balance += pnl - comm
        idea.log.append(f"{t} close {qty:.0f} @ {idea.direction * px:.5f} {reason} pnl {pnl - comm:.2f}")
        if idea.units_open <= 1e-9:
            idea.units_open = 0
            idea.status, idea.exit_reason, idea.exit_time = "closed", reason, str(t)

    # ---- daily: management
    def on_day_close(self, sd, day):
        p = self.p
        for idea in [x for x in self.active if x.symbol == sd.sym and x.live()]:
            v = sd.views[idea.direction]
            unfilled = [o for o in idea.orders if not o.filled and not o.cancelled]
            # expiry of unfilled orders
            if unfilled and day - idea.placed_day >= p["max_pending_days"]:
                for o in unfilled:
                    o.cancelled = True
            # bias break: daily close beyond A cancels unfilled orders
            if v.c[day] < idea.a:
                for o in unfilled:
                    o.cancelled = True
            if idea.status == "pending" and all(o.cancelled for o in idea.orders):
                idea.status, idea.exit_reason, idea.exit_time = "cancelled", "expired", str(sd.dates[day])
                continue
            if idea.status != "open":
                continue
            # break-even on a confirmed higher low above the average entry
            pls = known_pivots(v.pl_m, p["mgmt_pivot_bars"], day)
            if not idea.breakeven and p["breakeven_mode"] in ("tp1_or_higher_low", "higher_low_only"):
                for j in reversed(pls):
                    if j <= idea.first_fill_day:
                        break
                    if v.l[j] > idea.avg_entry():
                        idea.stop = max(idea.stop, idea.avg_entry())
                        idea.breakeven = True
                        idea.last_trail_pivot = j
                        break
            # trail behind each new confirmed swing low
            if idea.breakeven and p["trail_mode"] == "d1_structure" and pls:
                j = pls[-1]
                if j > idea.last_trail_pivot and j > idea.first_fill_day:
                    idea.stop = max(idea.stop, v.l[j] - p["trail_buffer_atr"] * v.atr[day])
                    idea.last_trail_pivot = j
            # maximum hold
            if day - idea.first_fill_day >= p["max_hold_days"]:
                x_adj = 0.0 if idea.direction == 1 else sd.spec["spread"]
                self.close_units(idea, idea.units_open, v.c[day] - x_adj, sd.dates[day], "max_hold")

    # ---- weekly: new setups
    def on_week_close(self, sd, day, t):
        p = self.p
        if sum(1 for x in self.ideas if x.symbol == sd.sym and x.live()) >= p["max_ideas_per_symbol"]:
            return
        week = sd.week_of_day[day]
        bias = weekly_bias(sd.views, week, p)
        if bias == 0:
            return
        v = sd.views[bias]
        st = find_setup(v, day, p, sd.spec["step"])
        if not st or (sd.sym, bias, st["ib"]) in self.used_b:
            return
        risk_usd = self.balance * p["risk_pct"] / 100.0
        if self.open_risk_pct() + p["risk_pct"] > p["max_open_risk_pct"] + 1e-9:
            return
        base, quote = sd.sym[:3], sd.sym[3:]
        if self.ccy_count(base, bias) >= p["max_same_ccy_dir"] or self.ccy_count(quote, -bias) >= p["max_same_ccy_dir"]:
            return
        conv = self.usd_per_quote(sd.sym, sd.dates[day])
        orders = []
        for pct, lv, share in st["levels"]:
            units = self.round_units(sd.sym, risk_usd * share / ((lv - st["stop"]) * conv))
            orders.append(Order(pct=pct, price=lv, risk_share=share, units=units))
        if not any(o.units > 0 for o in orders):
            return
        self.used_b.add((sd.sym, bias, st["ib"]))
        idea = Idea(id=self.next_id, symbol=sd.sym, direction=bias, a=st["a"], b=st["b"], ia=st["ia"], ib=st["ib"],
                    stop=st["stop"], tps=st["tps"], orders=orders, placed_day=day, placed_time=str(t),
                    risk_usd=risk_usd, r_tp3=st["r_tp3"])
        self.next_id += 1
        self.ideas.append(idea)
        self.active.append(idea)
