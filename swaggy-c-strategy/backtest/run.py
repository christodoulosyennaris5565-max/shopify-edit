"""Run the Swaggy C backtest and write a report.

    python run.py                                  # settings from ../strategy_params.yaml
    python run.py --risk 1.5 --balance 100000      # override the account settings
    python run.py --set stop_pct=78.6 --set max_hold_days=90 --name stop786

Outputs in results/<name>/: summary.md, trades.csv, equity.csv
"""
import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

from engine import Backtest, load_params

HERE = Path(__file__).parent


def parse_value(v):
    try:
        return json.loads(v)
    except json.JSONDecodeError:
        return v


def summarize(bt, p):
    ideas = [i for i in bt.ideas if i.first_fill_day >= 0]
    pnl = [i.pnl_usd for i in ideas]
    r = [i.pnl_usd / i.risk_usd for i in ideas]
    wins = [x for x in pnl if x > 0]
    losses = [x for x in pnl if x <= 0]
    eq = [e for _, _, e in bt.equity]
    peak, mdd, mdd_pct = -1e18, 0.0, 0.0
    for e in eq:
        peak = max(peak, e)
        mdd = max(mdd, peak - e)
        mdd_pct = max(mdd_pct, (peak - e) / peak * 100 if peak > 0 else 0)
    worst_day = 0.0
    for k in range(1, len(bt.equity)):
        prev = bt.equity[k - 1][2]
        worst_day = min(worst_day, (bt.equity[k][2] - prev) / prev * 100)
    streak = best = 0
    for x in pnl:
        streak = streak + 1 if x <= 0 else 0
        best = max(best, streak)
    years = max((bt.equity[-1][0] - bt.equity[0][0]).days / 365.25, 1e-9) if bt.equity else 1
    end = bt.equity[-1][2] if bt.equity else p["start_balance"]
    s = dict(
        start=str(bt.equity[0][0]) if bt.equity else "", end=str(bt.equity[-1][0]) if bt.equity else "",
        start_balance=p["start_balance"], end_equity=round(end, 2),
        net_profit=round(end - p["start_balance"], 2),
        cagr_pct=round(((end / p["start_balance"]) ** (1 / years) - 1) * 100, 2) if end > 0 else -100,
        ideas_placed=len(bt.ideas), ideas_filled=len(ideas),
        cancelled_unfilled=sum(1 for i in bt.ideas if i.first_fill_day < 0),
        win_rate_pct=round(len(wins) / len(ideas) * 100, 1) if ideas else 0,
        avg_r=round(sum(r) / len(r), 3) if r else 0,
        profit_factor=round(sum(wins) / -sum(losses), 2) if losses and sum(losses) < 0 else float("inf"),
        max_drawdown_pct=round(mdd_pct, 2), max_drawdown_usd=round(mdd, 2),
        worst_day_pct=round(worst_day, 2), longest_losing_streak=best,
        ideas_per_year=round(len(ideas) / years, 1),
    )
    fills = defaultdict(int)
    for i in ideas:
        for o in i.orders:
            if o.filled:
                fills[o.pct] += 1
    s["fills_by_level"] = {str(k): v for k, v in sorted(fills.items())}
    s["tp_reached"] = {f"tp{k}": sum(1 for i in ideas if i.max_tp >= k) for k in range(1, 5)}
    s["exit_reasons"] = dict(sorted(defaultdict(int, {}).items()))
    er = defaultdict(int)
    for i in ideas:
        er[i.exit_reason or "open"] += 1
    s["exit_reasons"] = dict(er)
    by_sym = defaultdict(lambda: [0, 0, 0.0])
    for i in ideas:
        b = by_sym[i.symbol]
        b[0] += 1; b[1] += i.pnl_usd > 0; b[2] += i.pnl_usd
    s["by_symbol"] = {k: dict(ideas=v[0], win_rate_pct=round(v[1] / v[0] * 100, 1), net=round(v[2], 2)) for k, v in sorted(by_sym.items())}
    by_year = defaultdict(lambda: [0, 0.0])
    for i in ideas:
        y = i.exit_time[:4] if i.exit_time else "open"
        by_year[y][0] += 1; by_year[y][1] += i.pnl_usd
    s["by_year"] = {k: dict(ideas=v[0], net=round(v[1], 2)) for k, v in sorted(by_year.items())}
    return s


def write(bt, p, s, out):
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "trades.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "symbol", "side", "placed", "A", "B", "stop", "tp1", "tp2", "tp3", "tp4", "orders_filled",
                    "avg_entry", "risk_usd", "pnl_usd", "r_multiple", "max_tp", "exit_reason", "exit_time"])
        for i in bt.ideas:
            d = i.direction
            w.writerow([i.id, i.symbol, "long" if d == 1 else "short", i.placed_time[:10], round(d * i.a, 5), round(d * i.b, 5),
                        round(d * i.stop, 5)] + [round(d * x, 5) for x in i.tps] +
                       ["/".join(str(o.pct) for o in i.orders if o.filled), round(d * i.avg_entry(), 5) if i.first_fill_day >= 0 else "",
                        round(i.risk_usd, 2), round(i.pnl_usd, 2), round(i.pnl_usd / i.risk_usd, 3), i.max_tp, i.exit_reason, i.exit_time[:16]])
    with open(out / "equity.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "balance", "equity"])
        for dt, b, e in bt.equity:
            w.writerow([dt, round(b, 2), round(e, 2)])
    lines = [f"# Backtest: {out.name}", "", "## Settings", "```", json.dumps({k: v for k, v in p.items()}, indent=1, default=str), "```",
             "", "## Results", "```", json.dumps(s, indent=1), "```"]
    (out / "summary.md").write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default=str(HERE.parent / "strategy_params.yaml"))
    ap.add_argument("--data", default=str(HERE / "data"))
    ap.add_argument("--risk", type=float)
    ap.add_argument("--balance", type=float)
    ap.add_argument("--symbols", nargs="+")
    ap.add_argument("--set", action="append", default=[], help="key=value override, e.g. stop_pct=78.6")
    ap.add_argument("--name", default="baseline")
    a = ap.parse_args()
    ov = {}
    if a.risk is not None:
        ov["risk_pct"] = a.risk
    if a.balance is not None:
        ov["start_balance"] = a.balance
    if a.symbols:
        ov["symbols"] = a.symbols
    for kv in a.set:
        k, v = kv.split("=", 1)
        ov[k] = parse_value(v)
    p = load_params(a.params, ov)
    bt = Backtest(a.data, p).run()
    s = summarize(bt, p)
    out = HERE / "results" / a.name
    write(bt, p, s, out)
    print(json.dumps(s, indent=1))
    print(f"\nWritten to {out}")


if __name__ == "__main__":
    main()
