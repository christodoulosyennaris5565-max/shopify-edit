"""Swaggy C position-trading strategy: core logic (no I/O, no pandas).

Written to port 1:1 to a cTrader cBot (C#):
- plain classes, lists and loops
- every price comparison is done in "long space": a short setup is evaluated on
  flipped prices (x -> -x, so highs become lows). One code path serves both
  directions. In C# keep the same trick, or duplicate the branches.
- swing points (pivots) are precomputed once; a pivot at bar i is only *known*
  at bar i + n, and every lookup below respects that (no look-ahead).

Rules follow BACKTEST_SPEC.md; numbers come from strategy_params.yaml.
"""
import bisect
import math
from dataclasses import dataclass, field
from typing import List


# ---------------------------------------------------------------- indicators

def ema(values, period):
    out, k = [], 2.0 / (period + 1)
    for i, v in enumerate(values):
        out.append(v if i == 0 else v * k + out[-1] * (1 - k))
    return out


def atr(highs, lows, closes, period):
    """Wilder ATR; value at i uses bars 0..i."""
    out, prev_close, a = [], None, None
    for i in range(len(highs)):
        tr = highs[i] - lows[i] if prev_close is None else max(
            highs[i] - lows[i], abs(highs[i] - prev_close), abs(lows[i] - prev_close))
        a = tr if a is None else ((a * i + tr) / (i + 1) if i < period else (a * (period - 1) + tr) / period)
        out.append(a)
        prev_close = closes[i]
    return out


def pivot_highs(highs, n):
    """Swing highs: higher than the n bars before, not exceeded by the n bars after."""
    return [i for i in range(n, len(highs) - n)
            if all(highs[i] > highs[j] for j in range(i - n, i))
            and all(highs[i] >= highs[j] for j in range(i + 1, i + n + 1))]


def pivot_lows(lows, n):
    return [i for i in range(n, len(lows) - n)
            if all(lows[i] < lows[j] for j in range(i - n, i))
            and all(lows[i] <= lows[j] for j in range(i + 1, i + n + 1))]


def known_pivots(pivots, n, today):
    """Pivots already confirmed at bar `today` (pivot index <= today - n)."""
    k = bisect.bisect_right(pivots, today - n)
    return pivots[:k]


# ---------------------------------------------------------------- Fibonacci

def fib_level(a, b, pct):
    """A = 100%, B = 0% (long space: A below B). Negative pct = extension beyond B."""
    return b + (a - b) * pct / 100.0


def next_round_beyond(price, step):
    """Next round number strictly above price (long space; works for negated prices too)."""
    r = math.ceil(price / step - 1e-9) * step
    return r + step if r <= price + 1e-12 else r


# ---------------------------------------------------------------- price views

class View:
    """Daily + weekly bars for one symbol in one direction (long space)."""

    def __init__(self, d_o, d_h, d_l, d_c, w_h, w_l, w_c, p):
        self.o, self.h, self.l, self.c = d_o, d_h, d_l, d_c
        self.w_h, self.w_l, self.w_c = w_h, w_l, w_c
        self.atr = atr(d_h, d_l, d_c, p["atr_period"])
        n, m, wn = p["pivot_bars"], p["mgmt_pivot_bars"], p["bias_pivot_bars"]
        self.ph = pivot_highs(d_h, n)          # setup swing highs (B)
        self.pl_m = pivot_lows(d_l, m)         # management swing lows (break-even / trail)
        self.w_ph = pivot_highs(w_h, wn)
        self.w_pl = pivot_lows(w_l, wn)
        self.w_ema_f = ema(w_c, p["ema_fast"])
        self.w_ema_s = ema(w_c, p["ema_slow"])


def flip(seq):
    return [-x for x in seq]


def make_views(d, w, p):
    """d/w: dicts of lists open/high/low/close. Returns {+1: View, -1: View}."""
    long_v = View(d["open"], d["high"], d["low"], d["close"], w["high"], w["low"], w["close"], p)
    short_v = View(flip(d["open"]), flip(d["low"]), flip(d["high"]), flip(d["close"]),
                   flip(w["low"]), flip(w["high"]), flip(w["close"]), p)
    return {1: long_v, -1: short_v}


# ---------------------------------------------------------------- bias (weekly)

def weekly_bias_long(v, week, p):
    """True if the long-space weekly chart is bullish using weeks 0..week (all closed)."""
    n = p["bias_pivot_bars"]
    hs = known_pivots(v.w_ph, n, week)
    ls = known_pivots(v.w_pl, n, week)
    if len(hs) < 2 or len(ls) < 2:
        return False
    if not (v.w_h[hs[-1]] > v.w_h[hs[-2]] and v.w_l[ls[-1]] > v.w_l[ls[-2]]):
        return False
    return (not p["use_weekly_ema"]) or v.w_ema_f[week] > v.w_ema_s[week]


def weekly_bias(views, week, p):
    if weekly_bias_long(views[1], week, p):
        return 1
    if weekly_bias_long(views[-1], week, p):
        return -1
    return 0


# ---------------------------------------------------------------- setup

def find_setup(v, today, p, step):
    """New Fib ladder from daily bars 0..today (all closed), long space. None if no valid setup."""
    n = p["pivot_bars"]
    ph = known_pivots(v.ph, n, today)
    if not ph:
        return None
    ib = ph[-1]
    b = v.h[ib]
    start = ph[-2] + 1 if len(ph) > 1 else max(0, ib - 60)
    ia = min(range(start, ib + 1), key=lambda j: v.l[j])
    a = v.l[ia]
    if b - a < p["min_impulse_atr"] * v.atr[ib]:
        return None
    after = range(ib + 1, today + 1)
    if any(v.h[j] > b for j in after):
        return None                                     # new high since B: wait for a new swing
    stop = fib_level(a, b, p["stop_pct"]) - p["stop_buffer_atr"] * v.atr[today]
    low_since = min((v.l[j] for j in after), default=float("inf"))
    if low_since <= stop:
        return None
    tps = [fib_level(a, b, t) for t in p["targets_pct"]]
    tps.append(next_round_beyond(tps[-1], step))
    levels = []
    for pct, share in zip(p["ladder_pct"], p["ladder_share"]):
        lv = fib_level(a, b, pct)
        if share > 0 and low_since > lv:                # skip levels price already traded through
            levels.append((pct, lv, share))
    if not levels:
        return None
    tot = sum(s for _, _, s in levels)
    r_tp3 = sum(s * (tps[2] - lv) / (lv - stop) for _, lv, s in levels) / tot
    if r_tp3 < p["min_rr"]:
        return None
    return dict(a=a, b=b, ia=ia, ib=ib, stop=stop, tps=tps, levels=levels, r_tp3=r_tp3)


# ---------------------------------------------------------------- trade state

@dataclass
class Order:
    pct: float
    price: float          # long space
    risk_share: float
    units: float = 0.0
    filled: bool = False
    cancelled: bool = False
    fill_price: float = 0.0
    fill_time: str = ""


@dataclass
class Idea:
    id: int
    symbol: str
    direction: int
    a: float
    b: float
    ia: int
    ib: int
    stop: float
    tps: List[float]
    orders: List[Order]
    placed_day: int
    placed_time: str
    risk_usd: float
    r_tp3: float
    tp_hit: List[bool] = field(default_factory=lambda: [False] * 4)
    status: str = "pending"          # pending -> open -> closed | cancelled
    first_fill_day: int = -1
    units_at_tp1: float = 0.0
    units_open: float = 0.0
    breakeven: bool = False
    last_trail_pivot: int = -1
    pnl_usd: float = 0.0
    costs_usd: float = 0.0
    exit_reason: str = ""
    exit_time: str = ""
    max_tp: int = 0
    log: List[str] = field(default_factory=list)

    def avg_entry(self):
        f = [o for o in self.orders if o.filled]
        u = sum(o.units for o in f)
        return sum(o.fill_price * o.units for o in f) / u if u else 0.0

    def units_filled(self):
        return sum(o.units for o in self.orders if o.filled)

    def live(self):
        return self.status in ("pending", "open")
