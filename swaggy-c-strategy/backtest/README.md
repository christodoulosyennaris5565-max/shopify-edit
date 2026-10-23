# Swaggy C strategy: backtest code

Python backtest of the rules in [../BACKTEST_SPEC.md](../BACKTEST_SPEC.md), using the settings in [../strategy_params.yaml](../strategy_params.yaml). It is written so it can be ported line by line to a cTrader cBot (C#).

## Files

| File | What it does |
|---|---|
| `duka.py` | Downloads spot FX and gold prices (BID) from Dukascopy, from 2014, and builds daily bars. |
| `strategy.py` | The trading rules: indicators, swing points, weekly bias, finding the Fib setup, order and trade objects. No file or network access. This is the part to port to C#. |
| `engine.py` | Runs the rules through history: limit fills, stops, targets, break-even, trailing, time exits, portfolio limits, dollar maths. |
| `run.py` | Runs a backtest and writes `results/<name>/summary.md`, `trades.csv`, `equity.csv`. |
| `test_strategy.py` | Checks the Fib maths against the worked USD/JPY example and runs the engine on synthetic data. |

## How to run

```bash
pip install pyyaml
python duka.py download-daily --out data     # daily bars, 2014 -> last month (slow: Dukascopy throttles)
python duka.py build-daily --out data
python test_strategy.py
python run.py --risk 1.5 --balance 100000 --name baseline
python run.py --risk 1.5 --set stop_pct=78.6 --name stop_786      # test another setting
```

Any setting from `load_params()` in `engine.py` can be changed with `--set key=value`. Examples:
- `ladder_share=[0.33,0.33,0.34]`
- `close_fractions=[0.1,0.2,0.3,0.4]`
- `max_hold_days=90`
- `breakeven_mode="tp1_only"`
- `trail_mode="none"`

## Current test setup (user)

- Account: $100,000.
- Risk: 1.5% per idea. That's the total if all three ladder orders fill.
- Max open risk: 4.5%, i.e. 3 ideas.
- Pairs:
  - USD/JPY, GBP/AUD, USD/CAD, GBP/USD, XAU/USD.
  - EUR/USD and AUD/USD are downloaded too: they're used for dollar conversion and can be tested.
- Period: January 2014 (when he started trading) to the latest full month.

## How the engine works

These are the events a cBot would use:

| Python | cBot equivalent | What happens |
|---|---|---|
| `process_hour` | `OnBar` (H1), or `OnTick` | Limit fills, stop hits, take-profit hits |
| `on_day_close` | Daily bar closes | Order expiry, bias break, break-even, trailing, 60-day time exit |
| `on_week_close` | Weekly bar closes | Weekly bias, find the Fib swing, place the limit ladder |

**Long space.** A short setup is handled by flipping prices (x → −x), so one code path serves both directions. In C#, either keep the trick or write mirrored branches.

**No look-ahead.** A swing point at bar i is only used from bar i + n, when it is confirmed.

**Cost model:**
- Prices are BID.
  - A buy limit fills when the ask (bid + spread) reaches it.
  - A short's stop and targets trigger on the ask.
- Stops get 0.5 pip of slippage.
- Commission is $7 per lot, round trip.
- The spread for each symbol is in `SPECS` in `engine.py`.

**Sizing:**
- Each order's lots are set so the order loses its share of the 1.5% at the stop.
- Lots are rounded down to 0.01, as a cBot would round volume.
- Dollar conversion uses USD/JPY, USD/CAD, AUD/USD, GBP/USD and EUR/USD closes, not a fixed $10 per pip.

## Known limits of the first test

1. **Daily-fill mode.** Dukascopy throttles cloud servers heavily, so the first test uses daily bars for fills (`data/MODE` says which mode is active).
   - Inside one day the engine can't tell what happened first.
   - It assumes the worst case: stop before target, and an order filled that day can be stopped that day but can't take profit the same day.
   - Hourly data, which the engine already supports, will make fills more accurate once it downloads.
2. **Bar timing.** Daily bars for finished years are Dukascopy's UTC-midnight candles. Brokers and TradingView usually close the day at 17:00 New York, so swing points can differ slightly from his charts. The current year uses New York-close days built from hourly data.
3. **No swap (overnight financing).** This understates costs on long holds; it can be added per pair once you have your broker's swap rates.
4. **No news filter.** No historical calendar is connected yet, so the Blaze Funded ±3-minute rule isn't applied. Its effect on a daily-bar strategy is small, but it will matter in the cBot.
5. **Discretion not coded.** Trendline touches and "ugly chart" judgement are left out, as noted in the spec.
