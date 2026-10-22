# Backtest spec: Swaggy C position-trading strategy (v1 baseline)

This turns his 2025–2026 position-trading strategy (see [MASTER_STRATEGY.md](MASTER_STRATEGY.md)) into exact rules a program can follow. Where he never gives a rule, a **baseline default** is set so the strategy can be built and tested. All values live in [strategy_params.yaml](strategy_params.yaml).

**Labels used below**
- **USER**: set by you.
- **STATED**: he says it in a video.
- **VISUAL**: seen on his chart but not said.
- **BASE**: our default where he gives no rule. Every BASE value has a test range and should be checked in the backtest.

---

## 1. One-line summary

On the weekly chart, decide the direction. On the daily chart, find the latest impulse swing in that direction and draw a Fibonacci on it. Place 3 limit orders at 38.2 / 50 / 61.8 with one stop at 89.3, risking 1% of the account in total. Take profit in four steps at 0 / −27 / −61.8 / the next round number. Move to break-even after a higher low, then trail behind daily structure.

## 2. Fibonacci convention

This matches his charts (VISUAL).
- **Long:** A = swing low = 100%, B = swing high = 0%.
- **Short:** A = swing high = 100%, B = swing low = 0%.
- `level(p) = B + (A − B) × p / 100`
  - Retracements use positive p (38.2, 50, 61.8, 78.6, 89.3, 100).
  - Extensions use negative p (−27, −61.8) and land beyond B.

## 3. Rules, step by step

### 3.1 Schedule
Run the analysis on the first daily bar of each week (Monday), the way he does on Sunday/Monday (STATED). Pending orders and open trades are managed on every bar.

### 3.2 Direction (the "3-month bias")
| Rule | Default | Basis |
|---|---|---|
| Long bias | The weekly chart's last two confirmed swings are a higher high and a higher low, **and** the weekly EMA 8 is above the EMA 14 | BASE (his tools, our formula) |
| Short bias | The mirror: a lower high and a lower low, and the weekly EMA 8 is below the EMA 14 | BASE |
| No bias | Anything else. No new ideas on that symbol | BASE |
| Weekly swing pivot | 2 bars each side | BASE (test 2–3) |
| Only trade with the bias, never counter-trend | Always | STATED |

**Note:** he never explains how he picks the 3-month target. His examples line up with the Fib −27 / −61.8 extensions and the next round number, so the targets below double as his "3-month destination".

### 3.3 Finding the swing (A and B)
1. **Swing points.** On the daily chart, a swing high or low is a pivot with 5 bars on each side (BASE, test 3–10). Use wicks, not closes (VISUAL).
2. **Choosing A and B.**
   - **Long:** B = the most recent confirmed swing high. A = the lowest swing low before B since the previous swing high.
   - **Short:** the mirror.
3. **Size filter.** A to B must be at least 3 × ATR(14) on the daily chart (BASE, test 2–5). This filters out small swings he would ignore.
4. **Direction filter.** The swing must point in the bias direction (STATED).
5. **New extreme.** If price makes a new extreme beyond B before any order fills, re-anchor to the new B and cancel the old orders (BASE).

### 3.4 Entries
| Rule | Default | Basis |
|---|---|---|
| Order type | Limit orders only | STATED |
| Levels | 38.2, 50, 61.8 | STATED |
| Risk split across levels | 20% / 30% / 50% of the idea's risk | BASE ("61.8 gets the most, 38.2 the least" is STATED; the ratio is ours) |
| When to place | As soon as B is confirmed and price hasn't yet touched 38.2. If price is already past a level, skip that level | BASE |
| Cancel unfilled orders when | TP1 is hit, a new extreme forms beyond B, the stop is hit, or 20 days pass | BASE (test 10 / 20 / 40 days) |
| Optional filters (off in v1) | Round number within 0.5 × ATR of the 50/61.8; daily EMA 8/14 aligned; third trendline touch | BASE |

### 3.5 Stop loss
- One shared stop for every order in the idea, at **89.3%**, the midpoint of 78.6 and 100 (STATED: "middle of the 78.6 and the 100").
- On his USD/JPY chart the stop sat between 78.6 and 89.3 (VISUAL), so test 78.6 / 85 / 89.3 / 95 / 100.
- The stop never widens.

### 3.6 Position size (1% risk)
- **Risk per idea = 1% of the account balance when the orders are placed (USER).**
- Each order's dollar risk = 1% × its split share:
  - 38.2 order: 0.20%
  - 50 order: 0.30%
  - 61.8 order: 0.50%
- Lots = order risk ÷ (stop distance in pips × pip value per lot). Take pip value from the broker's contract spec, not his "$10 a pip" shorthand, which is wrong for JPY and AUD-quoted pairs.
- **If every order fills and the stop is hit, the loss is exactly 1%.** If only some orders fill, the loss is smaller.
- **Minimum reward check (STATED: ≥ 1:3).** Add up each order's reward at TP3 in R, weighted by its risk share. Skip the idea if the total is below 3.0 R (test 2–4).

### 3.7 Take profit
| Target | Level | Close (share of original size) | Basis |
|---|---|---|---|
| TP1 | 0% (B) | 25% | Level STATED; share BASE |
| TP2 | −27 | 25% | Level STATED; share BASE |
| TP3 | −61.8 | 25% | Level STATED; share BASE |
| TP4 | Next round number beyond TP3 | 25% (the rest) | Level STATED; share BASE |

- Round-number spacing:
  - USD/JPY: 5.00
  - GBP/AUD, USD/CAD and other majors: 0.025
  - Gold: 100
  - Basis: VISUAL for USD/JPY, GBP/AUD, USD/CAD and gold; BASE for the rest.
- Close-share sets to test:
  - 10/20/30/40 (his 2025 numbers)
  - 60/20/10/10 (his 2023 habit)
  - 0/50/50/0

### 3.8 Managing the trade
| Rule | Default | Basis |
|---|---|---|
| Move to break-even | First of: TP1 is hit, or a confirmed daily higher low forms above the average entry (3-bar pivot) | STATED (trigger), BASE (pivot size) |
| Break-even level | Exactly the average entry price, offset 0 | VISUAL (he drags it to exactly break-even) |
| Trail | After break-even, move the stop to 0.1 × ATR beyond each new confirmed daily swing low (long) or high (short) | STATED (trail by structure), BASE (buffer) |
| Maximum hold | 60 trading days, then close the rest at market | BASE (he holds "5 days to 2 months", aims ~3 months out; test 30 / 60 / 90) |
| Weekends | Hold | STATED |
| Swap | Include in results | STATED (he accepts swap as a cost) |
| Re-entry | Allowed on a new valid A–B swing in the bias direction | STATED |
| Bias break | If the setup's daily swing low (long) is broken on a daily close, cancel pending orders. Open trades keep their stop | STATED / BASE |

### 3.9 Portfolio limits
| Rule | Default | Basis |
|---|---|---|
| Ideas per symbol | 1 | BASE |
| Maximum total open risk | 3% | BASE (test 2 / 3 / 5) |
| Same currency, same direction | Max 2 ideas (e.g. long USD/JPY + long USD/CAD = 2 × long USD) | BASE |
| Symbols | USD/JPY, GBP/AUD, USD/CAD, GBP/USD, gold. Optional: EUR/USD, AUD/USD, GBP/JPY | STATED (his 2025–26 examples) |

### 3.10 News (Blaze Funded rule)
- No trade may open, fill or close from 3 minutes before to 3 minutes after a high-impact (red folder) Forex Factory event for that symbol's currencies.
- **Live:** cancel pending orders 3 minutes before the event and re-place them 3 minutes after.
- **Backtest:** drop any fill or exit that lands inside a window. Then report how many trades that removed.

## 4. Worked example: his USD/JPY long (April 2026 video)

A = 146.662 (September 2025 low), B = 159.458 (January 2026 high). The swing is 12.796, about 1,280 pips. These are the anchors read from his chart.

| | Level | Price |
|---|---|---|
| Entry 1 (20% of risk) | 38.2 | 154.570 |
| Entry 2 (30% of risk) | 50 | 153.060 |
| Entry 3 (50% of risk) | 61.8 | 151.550 |
| Stop | 89.3 | 148.031 |
| TP1 | 0 | 159.458 |
| TP2 | −27 | 162.913 |
| TP3 | −61.8 | 167.366 |
| TP4 | Next 5.00 round number | 170.000 |

On a $100,000 account, 1% = $1,000 total risk:
- 38.2 order: $200 at risk, 653.9-pip stop. Reward at TP3 is 1.96 R.
- 50 order: $300 at risk, 502.9-pip stop. Reward at TP3 is 2.84 R.
- 61.8 order: $500 at risk, 351.9-pip stop. Reward at TP3 is 4.49 R.

The risk-weighted reward at TP3 is 3.49 R, above the 3.0 R minimum, so the setup is valid.

**Check against his chart:**
- **Entry:** his real entry was 152.835, between our 50 and 61.8 levels.
- **Stop:** his stop was 148.518, a little tighter than our 89.3.
- **Targets:** his TP4 was 170.048; our 170.000 matches it.

His TP2 and TP3 ("163" and "167") also match ours. Use this example as a test case for the code.

## 5. Uncertain items: baseline chosen and what to test

| # | Uncertain item | Baseline | Test | How to judge |
|---|---|---|---|---|
| 1 | Risk per trade | **1% per idea (USER)** | 0.5 / 1 / 1.5 / 2 | Drawdown vs prop limits |
| 2 | Split across the 3 orders | 20/30/50 | Equal thirds; 0/40/60; 61.8 only | Return per unit of drawdown; fill rate |
| 3 | Which swing to anchor the Fib on | Daily 5-bar pivots, ≥ 3 × ATR | Pivots 3/5/8/10; ATR 2–5×; weekly swings | Number of setups vs win rate |
| 4 | When to place the orders | When B is confirmed | Also: wait for the first daily close back below B | Missed-trade count |
| 5 | Unfilled orders | Cancel at TP1, new extreme, or after 20 days | 10 / 40 days | Late fills that lose |
| 6 | Stop level | 89.3 | 78.6 / 85 / 95 / 100 | Stop-outs that later hit TP1 |
| 7 | Profit split | 25/25/25/25 | 10/20/30/40; 60/20/10/10; 0/50/50/0 | Average R per idea |
| 8 | How to pick the 3-month direction | Weekly structure + weekly EMA 8/14 | Structure only; EMA only | Ideas against the later move |
| 9 | Break-even trigger | TP1 or a daily higher low | TP1 only; higher low only; never | Trades stopped at break-even that later hit TP3 |
| 10 | Trailing | Daily structure | Weekly structure; no trail | Average R of runners |
| 11 | Maximum hold | 60 days | 30 / 90 | Return of trades closed by time |
| 12 | EMAs (settings hidden on screen) | 8 and 14 EMA on weekly closes | SMA 8/14; 8/16; off | Bias accuracy |
| 13 | Round-number zones | Not required in v1 | Require one within 0.5 × ATR | Win rate with vs without |
| 14 | Trendline third touch | Not used in v1 | Add later by hand or with a detector | Same |
| 15 | Which pairs | 5 core pairs | Each pair on its own; add optional pairs | Per-pair results |
| 16 | Total exposure | 3% open; max 2 same currency and direction | 2% / 5%; 1 / 3 | Worst drawdown |
| 17 | Daily vs weekly Fib (he says both) | Daily | Weekly | Results by era |
| 18 | Pip value (his $10 a pip is wrong) | Broker contract spec | n/a | Correct dollar maths |
| 19 | News | Block ±3 minutes (firm rule) | n/a | Trades removed |
| 20 | Ladder vs "average down" rule | Pre-placed ladder, one fixed stop | n/a | **Ask Blaze Funded support before going live** |

## 6. What the backtest should report
- Totals:
  - number of ideas and orders filled
  - win rate per idea
  - average R
  - expectancy
  - profit factor
- Risk:
  - worst drawdown
  - worst day
  - longest losing streak
- Fills:
  - how often each ladder level fills
  - share of ideas where only the 38.2 order fills
- Targets: how often each TP is reached.
- Splits:
  - results per symbol
  - results per period (2015–2019, 2020–2022, 2023–latest)
- Prop check: pass or fail against the Blaze Funded account's daily-loss and maximum-drawdown limits. Enter those in `prop_firm_checks` before running.
- Comparison to his claims: about 14 trades a quarter, 70–80% win rate, 1:3+ reward. Treat these as his claims, not targets.

## 7. Known limits of this spec
- Many v1 rules are our defaults, not his rules (every **BASE** row). They are starting points to test, not a copy of what he does.
- His discretionary filters aren't coded in v1:
  - trendline touches
  - "ugly chart" judgement
  - news reading
  - choosing which pairs to focus on

  Expect live results from his own discretion to differ.
- The worked example is the only setup with chart-verified anchors. More of his 2026 trades (USD/CAD, GBP/AUD in the [chart notes](videos/2026-visual-chart-notes.md)) can be added as test cases.
