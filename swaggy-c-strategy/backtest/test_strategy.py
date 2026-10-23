"""Checks for the strategy code. Run: python test_strategy.py

1. Fib maths matches the worked USDJPY example in BACKTEST_SPEC.md section 4.
2. The full engine runs end to end on synthetic data (no real-data claims).
"""
import math
import random
import tempfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from strategy import fib_level, next_round_beyond


def test_worked_example():
    a, b = 146.662, 159.458
    want = {38.2: 154.570, 50: 153.060, 61.8: 151.550, 89.3: 148.031, 0: 159.458, -27: 162.913, -61.8: 167.366}
    for pct, price in want.items():
        got = fib_level(a, b, pct)
        assert abs(got - price) < 0.001, (pct, got, price)
    assert abs(next_round_beyond(fib_level(a, b, -61.8), 5.0) - 170.0) < 1e-9
    # short side in long space: negate prices, same maths
    assert abs(-fib_level(-b, -a, 61.8) - (a + (b - a) * 0.618)) < 1e-9
    assert next_round_beyond(-167.366, 5.0) == -165.0
    print("worked example: OK")


def make_synthetic(folder, sym="USDJPY", start=date(2014, 1, 1), days=3000, seed=7):
    """Trending random walk with pullbacks, hourly bars, NY-close daily bars."""
    from duka import NY
    random.seed(seed)
    px, t = 105.0, datetime(start.year, start.month, start.day, tzinfo=timezone.utc)
    hourly = []
    regime = 1
    for h in range(days * 24):
        if h % (24 * 120) == 0:
            regime = random.choice([1, 1, -1])
        if t.weekday() >= 5 and not (t.weekday() == 6 and t.hour >= 22):
            t += timedelta(hours=1)
            continue
        drift = regime * 0.0012 * math.sin(h / (24 * 9.0)) + regime * 0.0006
        o = px
        c = px + drift + random.gauss(0, 0.06)
        hi, lo = max(o, c) + abs(random.gauss(0, 0.04)), min(o, c) - abs(random.gauss(0, 0.04))
        hourly.append((t, o, hi, lo, c))
        px, t = c, t + timedelta(hours=1)
    (folder / "hourly").mkdir(parents=True)
    (folder / "daily").mkdir()
    with open(folder / "hourly" / f"{sym}.csv", "w") as f:
        f.write("time_utc,open,high,low,close\n")
        for r in hourly:
            f.write(f"{r[0]:%Y-%m-%d %H:%M:%S},{r[1]:.3f},{r[2]:.3f},{r[3]:.3f},{r[4]:.3f}\n")
    daily = {}
    for ts, o, hi, lo, c in hourly:
        d = (ts.astimezone(NY) + timedelta(hours=7)).date()
        if d.weekday() >= 5:
            continue
        if d not in daily:
            daily[d] = [o, hi, lo, c]
        else:
            x = daily[d]
            x[1], x[2], x[3] = max(x[1], hi), min(x[2], lo), c
    with open(folder / "daily" / f"{sym}.csv", "w") as f:
        f.write("date,open,high,low,close\n")
        for d in sorted(daily):
            f.write(f"{d},{daily[d][0]:.3f},{daily[d][1]:.3f},{daily[d][2]:.3f},{daily[d][3]:.3f}\n")


def test_engine_runs():
    from engine import Backtest, load_params
    from run import summarize
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        make_synthetic(folder)
        p = load_params(Path(__file__).parent.parent / "strategy_params.yaml",
                        {"symbols": ["USDJPY"], "risk_pct": 1.5, "start_balance": 100000})
        bt = Backtest(folder, p).run()
        s = summarize(bt, p)
        assert s["ideas_placed"] > 0, "no setups found on synthetic data"
        # invariants
        for i in bt.ideas:
            d = i.direction
            assert i.stop < min(o.price for o in i.orders) or i.breakeven, "stop must sit beyond every entry"
            assert i.tps == sorted(i.tps), "targets must step outward"
            if i.first_fill_day >= 0 and not i.breakeven and i.exit_reason == "stop":
                assert i.pnl_usd >= -i.risk_usd * 1.10, f"loss larger than planned risk: {i.pnl_usd} vs {i.risk_usd}"
        print("engine on synthetic data: OK", {k: s[k] for k in ("ideas_placed", "ideas_filled", "win_rate_pct", "avg_r")})


if __name__ == "__main__":
    test_worked_example()
    test_engine_runs()
