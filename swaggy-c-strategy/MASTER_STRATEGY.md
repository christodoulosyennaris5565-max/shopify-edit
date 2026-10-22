# Chris "Swaggy C" Williams: Master Strategy Document

Synthesised from 45 per-video write-ups (2020-02 to 2026-10), the Shorts write-up (53 Shorts, 2021-09 to 2026-10), the video index, and spot-checks of the raw transcripts. Written 2026-10-22.

**How to read the citations**

- Format: (upload date, videoId, [m:ss]). Timestamps mark the start of the ~60-second caption block that holds the quote, not the exact second.
- Quotes are his own words from auto-captions. Obvious caption errors are fixed, and uncertain words are marked [?].
- Every rule in Section 2 has one of three labels:
  - **STATED**: he says it as a rule or as what he does.
  - **INFERRED**: it holds across his examples, but he never states it as a rule.
  - **CARRIED OVER**: it was defined in an older video and nothing in 2025-26 contradicts it. The source video is named.
- The most important current numbers were checked against the raw transcripts of 787JlWMtCwU, oUzc4qeRIhg, UXGnJ76wssE, TaH782wuq7Q and the 2025-26 Shorts (etjvn5pccyM, mLT7cdcn5Tg, tXz6sPJASKE). These are marked ✔ where it matters.
- A fourth label, **VISUAL**, marks something seen on his TradingView screen in the two April 2026 videos but not said aloud. The source is the frame-by-frame review in `videos/2026-visual-chart-notes.md`, cited as (VCN, <video>, <time>). It was read at 480p, so some values are derived from legible Fib levels.

---

## 1. Summary

1. Since 2025 he calls himself a **position trader**. He announced this in August 2025 and said he "developed [it] earlier this year" (2025-08-15, TaH782wuq7Q, [17:21]).
2. Each week, usually on a Sunday or Monday, he decides **where price will be in about 3 months** on the weekly/daily chart. He then takes **only trades in that direction**: no counter-trend trades and no "sniper" entries (2026-04-03, oUzc4qeRIhg, [13:19]-[14:19], [33:32]-[34:32]; 2026-04-04, 787JlWMtCwU, [8:08]-[9:08]).
3. His chart toolkit is unchanged from earlier years:
   - psychological round-number levels, drawn as **boxes**
   - trend lines
   - the **8 and 14 EMA**
   - a **Fibonacci A-B-C** drawn on the higher-timeframe swing.

   What changed is **entries, exits and holding time**: "the strategy is kind of the same, the entries and the exits are different… you're just holding it longer" (787JlWMtCwU, [5:06]).
4. **Entry:** after the swing high (Fib 0%) he places a ladder of **limit orders at about the 38.2, 50 and 61.8 retracements**. The deepest order (61.8) gets the biggest lot and the shallowest (38.2) the smallest (787JlWMtCwU, [15:09]).
5. **Stop:** one wide stop **midway between the 78.6 and the 100 retracement**. That can be 50 to about 400 pips depending on the pair and the swing (787JlWMtCwU, [16:10], [20:12]-[21:13]).
6. **Targets:** a ladder with alerts. **TP1 = Fib 0%**, **TP2 = -27 extension**, **TP3 = -61.8 extension**, **TP4 = the next big psychological level**. He takes partials at each one. He wants a reward of at least 3-5× the risk (787JlWMtCwU, [6:06], [17:10]-[18:12]).
7. **Management:** once price makes a **higher low** (for a long), he moves the stop to break-even and then into profit. After that he lets the trade run for **days to a couple of months** and pays the swap (787JlWMtCwU, [18:12]-[19:12]; oUzc4qeRIhg, [34:32]; TaH782wuq7Q, [15:19]).
8. **Frequency:** low. "Less than 10 trades a quarter" in 2025. "Five trades a month, six trades a month" in July 2026. "14 trades in a quarter" in an August 2026 Short. A+ setups only, even if that means a month with no trades.
9. **Where he trades:** recent examples are USDJPY, GBPAUD, GBPUSD, USDCAD and gold. In July 2026 he said gold "looks too ugly… I'm not trading it right now" (UXGnJ76wssE, [8:14]).
10. **Accounts:** he recommends running this style only on **six-figure prop-firm accounts** (100K/250K/500K), because small accounts have daily-loss limits that are too tight. A small **personal brokerage account** of $2K-$10K is also fine (787JlWMtCwU, [12:08]-[14:09]).
11. **Biggest gaps for a replica:** he never states:
    - his risk % per trade in this system
    - the exact lot split across the ladder
    - the exact Fib anchor rules and extension values
    - which timeframe the EMAs are read on now
    - a firm entry trigger beyond "price reaches the limit".

    He points viewers to his paid "Swaggy AI" and courses for "what my Fibonacci settings are" and EMA colours (787JlWMtCwU, [7:07]-[8:08]).

    The on-screen review fills part of this gap. His Fib template and anchoring are visible. Every position tool on screen shows **"Amount: 750"**, which suggests a **fixed $750 risk per trade**, but he never says so (VISUAL; VCN).

---

## 2. The current strategy (2025-2026 position trading): complete rulebook

### 2.1 Instruments

| Rule | Label | Source |
|---|---|---|
| Recent worked examples: **USDJPY ("UJ")**, **GBPAUD ("GA")**, **GBPUSD ("GU")**, **USDCAD**, **gold (XAUUSD)**. EURUSD appears only in hypotheticals. | STATED (examples) | 787JlWMtCwU [7:07]-[21:13]; oUzc4qeRIhg [18:22], [32:32]; UXGnJ76wssE [6:07]-[8:14] |
| In April 2026 his main focus was UJ: "Shows how much I really focus on UJ versus, you know, gold and GU." | STATED | 787JlWMtCwU [18:12] ✔ |
| Round-number levels matter "especially [for] majors." | STATED | 787JlWMtCwU [5:06] ✔ |
| **Gold is traded only when its chart is clean.** In July 2026: "Gold looks too ugly for me right now. That's why I'm not trading it right now." | STATED | UXGnJ76wssE [8:14] ✔ |
| In September 2025 gold was the headline instrument: "All you need to focus on is gold to change your life," with a position-trade thesis toward 5,000 (gold was about 3,700). | STATED (then) | Short tXz6sPJASKE (2025-09-23) [0:02]-[1:03] ✔ |
| Long-term gold views: "I believe gold will get to 6,000 oz" (787JlWMtCwU [18:12] ✔). "Gold is at 4,500, it's going to get to 5,000" was given as an example of a 3-month bias (oUzc4qeRIhg [13:19]). | STATED | as cited |
| Gold behaves differently for alert-based entries: "if you miss that alert by a couple hours, it's curtains." For gold he uses limits, not alerts. | STATED | 787JlWMtCwU [20:12] ✔ |
| Trade only a few instruments and skip any chart that looks "ugly". | INFERRED (2026) / CARRIED OVER (1-2 pairs: 2023-09-01, CdTM3LGt0dc [1:02]; core watch list of 4: 2023-12-20, 0yoVaP_NTFA [2:06]) | — |

**Avoided now:** any instrument whose chart is "ugly" or choppy (gold in July 2026). He no longer repeats his 2021 rule that GBPAUD and GBPJPY are "too volatile to just hold" (2021-02-15, nOK64T2hLe8, [4:04]). GBPAUD is now one of his main position trades, so treat that 2021 rule as superseded.

### 2.2 Timeframes, holding period, trade frequency

| Rule | Label | Source |
|---|---|---|
| Position trading means the **daily/weekly** chart: "Daily, weekly and you're looking to… get out in a week or 2 weeks or 3 weeks or 4 weeks or 6 weeks or 8 weeks… position trading goes longer and longer." | STATED | 787JlWMtCwU [2:04] ✔ |
| The Fib and TPs are read on the **weekly**: "What I do and I go to the weekly time frame" (UJ); "Let me go back to the weekly" (GA). | STATED | 787JlWMtCwU [17:10], [21:13] ✔ |
| The directional read is done on the **weekly**: "If you are looking at a weekly time frame… It's very clearly it's a Fibonacci, right? A, B, C, and then go up to D." | STATED | UXGnJ76wssE [1:04] ✔ |
| In 2025 he described the method on the **daily**: "using Fibonacci trend lines all the same stuff but doing it on a daily time frame." | STATED | TaH782wuq7Q [9:13] ✔ |
| **Match analysis timeframe to style.** Never analyse on 1m-15m for a position trade. | STATED | oUzc4qeRIhg [8:13] |
| **Holding period: days to months.** "You can alter it for 5 days, 7 days, 14 days, 12 days… There can be a balance between the patience of holding for months and not having patience at all." Beginners: "Let's try to do 12 days, 11 days, 9 days, 8 days versus, you know, two months. Start small." | STATED | UXGnJ76wssE [10:15] ✔ |
| You are **not** meant to hold for the full 3 months: "I'm not telling you to… just hold it for 3 months." You can take "10 trades over those 3 months." | STATED | oUzc4qeRIhg [13:19]-[14:19] ✔ |
| A group trade in mid-2026 took about **10 weeks**: flat for 2 weeks, in drawdown for 3 weeks, then reached target. The expectation is to "come back to it four, five, six, seven, eight, nine weeks later." | STATED | Short etjvn5pccyM (2026-10-06) [0:02]-[1:02] ✔ |
| **Frequency (see contradictions §6.1):** "literally take less than 10 trades a quarter" (Aug 2025). "I'm going to take five trades a month, six trades a month" (Jul 2026). "I can actually take 14 trades in a quarter" (Aug 2026 Short). | STATED | TaH782wuq7Q [5:07] ✔; UXGnJ76wssE [10:15] ✔; Short mLT7cdcn5Tg [0:02] ✔ |
| **Several trades in the same direction are fine:** "why would you not find 1 2 3 4 5 6 7 trades in that direction and just hold them?" | STATED | 787JlWMtCwU [9:08] ✔ |
| **A+ setups only:** "If it's not an A+ setup, I'm not trading. Even if that means I can't trade for a month, so be it because month number two will pay for months 1 2 3 4 and 5." | STATED | 787JlWMtCwU [25:18] ✔ |
| Not every day, or even every month, is a trading day: "There may even some months where the market is trash." | STATED | Short mLT7cdcn5Tg [0:02] ✔ |
| Sessions do not matter. You enter and exit when you choose: "you come in when you want. You take profit when you want." | STATED | TaH782wuq7Q [18:22] |

### 2.3 Chart setup

**Platform.** TradingView for analysis, alerts and Bar Replay (787JlWMtCwU [15:09]; oUzc4qeRIhg [10:16]). STATED. His execution platform today is not stated. In 2024 it was TradeLocker with 24K Markets, plus FundedNext and forex.com (2024-11-23, Q6WiIOUcR8k, [1:04]; Short MuzWLtG8Lk4). CARRIED OVER, may be outdated.

**Step 1: strip the chart clean.** "strip it clean" (787JlWMtCwU [5:06]). STATED.

**Step 2: psychological round-number levels, drawn as boxes (zones).** STATED.
- "These round numbers when it comes to these pairs, especially majors. Let's do 160. We'll do 155. We'll do 150" (USDJPY) (787JlWMtCwU [5:06] ✔).
- To place a line exactly: "click it and just go to coordinates and just write 160.000" (787JlWMtCwU [6:06] ✔).
- Then turn it into a zone: "I'll just draw a rectangle around on all of them. Because price never stops at a particular… number. It'll stop at a area. So, you kind of draw boxes around them" (787JlWMtCwU [6:06] ✔).
- Spacing shown for USDJPY: every 5.00 (145/150/155/160). Upside targets named: 163, 167, 170 (787JlWMtCwU [9:08], [18:12]).
- *CARRIED OVER, how he spaces levels on other pairs:*
  - Whole figures and "quarter" levels every 250 pips with mid-levels (e.g. 1.1000 / 1.1250 / 1.1500; AUDUSD 0.7750) (2021-03-06, dIhU-khdVYw, [37:36]-[38:36]).
  - "New set of 10 digits" levels (1.70, 1.80, 1.90) are the strongest (dIhU-khdVYw [34:35]).
  - In 2024 he marked weekly quarter levels on EURUSD (1.1000 / 1.0750 / 1.0500 majors, with 25-pip sub-levels) and turned each into a rectangle: "I use this as an area" (2024-11-23, Q6WiIOUcR8k, [4:06]-[5:07]).
  - A level counts only if price has respected it: "wick wick wick" (Q6WiIOUcR8k [5:07]).
  - He also adds non-round reaction levels where price "stopped here, stopped here" (2023-11-29, koKRQ_pPhjQ, [21:31]).
- *VISUAL (VCN, 787JlWMtCwU 5:00-6:40, 21:40):*
  - Levels are black horizontal lines wrapped in **thin purple rectangles**, about ±0.2-0.3 yen on USDJPY and about ±20 pips on GBPAUD.
  - Lines are placed by hand, so they are not exactly round: 155.080, 150.154, 145.046. Only 160.000 was typed exactly.
  - Spacing on screen: USDJPY every 5.00. GBPAUD every 250 pips (2.05 / 2.025 / 2.00 …), with purple zones only on 2.05 / 2.00 / 1.95 / 1.90. USDCAD 1.400 / 1.375. Gold every ~$100 (some $50).
  - Extra boxes: flipped prior highs/lows (thin light-blue outline), a base/range (big beige box), and the Fib-anchor swing low (yellow box).
- *Box height:* never stated aloud. See the visual estimates above. A 2020 video draws consolidation boxes "from wick top to body top" (2020-02-11, pfoK9v7j7hY, [15:09]). That is not confirmed for current level boxes.

**Step 3: trend lines.** STATED.
- "You can find, you know, inner trend lines, outer trend lines. Like just play around with it." He then simplified to "a one-liner now… just so I can, you know, focus" (787JlWMtCwU [7:07] ✔).
- He uses a **"third trend line bounce"** as an entry confluence (787JlWMtCwU [23:14] ✔).
- *CARRIED OVER:* "a third bounce actually validates the trend line." Two touches are only a "potential trend line" (2021-02-22, UsbZgSzvpJI, [31:20]). A trend-line break alone does not change the trend. Price must break, retest, and take out the structure low (koKRQ_pPhjQ [14:24]; UsbZgSzvpJI [32:20]-[33:20]).

**Step 4: moving averages, the 8 and 14 EMA.** STATED.
- "We already have our moving averages on, right? In terms of, you know, the 8 and 14 EMA" (787JlWMtCwU [7:07] ✔).
- Current use: re-entry after a "retest [of] the moving average" (787JlWMtCwU [11:08] ✔).
- *CARRIED OVER:*
  - Exponential type, 8 = blue and 14 = red. "Anytime the blue crosses over the red, price is in an uptrend" (2021-02-22, UsbZgSzvpJI, [16:13]).
  - Price above the EMAs = up, below = down (koKRQ_pPhjQ [13:23]).
  - Crossovers are judged on the 4H or daily, never the 15m (UsbZgSzvpJI [18:15]).
  - The MA is never the only reason to enter (UsbZgSzvpJI [17:14]).
  - In 2021 he also used a **20/50 EMA** for long-term bias (UsbZgSzvpJI [30:20]). That has not been mentioned since 2021, so do not assume it is still on the chart.
  - In late 2024 he said "for the most part it's usually just a simple 8 EMA" (Q6WiIOUcR8k [17:22]). In 2026 he is back to "8 and 14."
- **Not stated now:** colours and the timeframe the EMAs are read on. He sends viewers to his AI for "what are my EMAs and… what colors they should be" (787JlWMtCwU [8:08] ✔).
- *VISUAL:* every chart, on every timeframe, shows exactly **two thin MAs**: a fast blue/blue-grey line and a slow red/salmon line. The indicator legend is hidden, so the "8 and 14 EMA" type and periods **cannot be confirmed on screen** (VCN, both videos).

**Step 5: Fibonacci A-B-C on the higher-timeframe swing.** STATED.
- "I'm going to look at this from an overall… Fibonacci standpoint… A to B, A B C. And now, we see exactly where price wants to go" (787JlWMtCwU [8:08] ✔).
- **Levels named in 2026:** 0% (TP1); 38.2, 50, 61.8 (entries); 78.6 and 100 (stop goes between them); -27 extension (TP2); -61.8 extension (TP3) (787JlWMtCwU [15:09]-[18:12] ✔).
- *CARRIED OVER, anchoring and settings:*
  - Draw from the start of the impulse (A = 100%) to its end (B = 0%). In a downtrend that means top to bottom; in an uptrend, bottom to top (2020-04-03, 0z39pJSwy2o, [5:09], [14:15]).
  - The template he told viewers to copy: **0, 38.2, 50, 61.8, 78.6, 100, -27, -61.8** (0z39pJSwy2o [5:09]-[6:09]).
  - "23.6 is irrelevant" (2021-02-14, 3jF0xjtV6zk, [5:05]-[6:06]).
  - Draw to the true swing extreme before a **full** retracement of about 4-6 candles. One or two opposite candles do not count (3jF0xjtV6zk [7:07]-[8:07]).
  - The Fib must start from a confluence (a key level, an MA cross, a trend-line break, a double bottom/top), "not the middle of nowhere" (3jF0xjtV6zk [6:06]-[7:07]).
  - Once the extension target is hit, the Fib is "done". Delete it and draw the next one (3jF0xjtV6zk [8:07], [12:10]).
- **VISUAL, his actual 2026 Fib template (identical on every chart):** **-61.8, -27, 0, 23.6, 38.2, 50, 61.8, 78.6, 100**, with price and percent labels.
  - Colours: 0/23.6/100 grey, 38.2/50 red, 61.8 green, 78.6 light blue, extensions yellow/orange.
  - **23.6 is back on the template**, although in 2021 he called it "irrelevant". He never uses it for entries, stops or targets.
  - **Anchoring:** longs run **swing low = 100% → swing high = 0%**; shorts run swing high = 100% → swing low = 0%. The extensions therefore project beyond 0% in the trade direction.
  - He anchors on the **latest completed impulse on the daily/weekly**. Examples: USDJPY Sep-2025 low 146.662 → Jan-2026 high 159.458; GBPAUD 2.01523 → 1.87058; USDCAD 1.36698 → 1.39660.
  - The Fib is redrawn as new swings complete.

  Source: (VCN, 787JlWMtCwU 8:20-9:50, 21:40; oUzc4qeRIhg 32:20-36:20).
- **Naming note:** he calls the targets the "-27" and "-61.8" extensions. In 2022 he called the same levels "1.27" and "1.618", and also used a "1.80" extension (koKRQ_pPhjQ [12:22]-[13:23]). Whether his tool uses -0.27 or -0.272 is never read out.

**Step 6: alerts.** STATED. He sets price alerts at each TP level (0%, -27, -61.8, the psych target) and optionally at the entry levels instead of placing limits (787JlWMtCwU [18:12]-[19:12] ✔).

**Platform details (VISUAL):** TradingView, light theme. Data feeds: OANDA for USDJPY and XAUUSD, FOREXCOM for GBPAUD. Watchlist: XAUUSD, BTCUSD, USDJPY, GBPUSD, GBPAUD, 6J1! (yen futures). Analysis is shown only on the **daily and weekly**. The 15m appears only to show noise or to zoom into an open trade (VCN).

### 2.4 Weekly routine

| Step | Label | Source |
|---|---|---|
| 1. **Analyse once, on a Sunday or Monday**, "for a good amount of time." | STATED | oUzc4qeRIhg [33:32]-[34:32] ✔ |
| 2. Decide the 3-month direction (see §2.5). | STATED | oUzc4qeRIhg [13:19] ✔ |
| 3. **Place a buy limit or sell limit.** "Place it, let it… come to you, place… one or two trades in that direction, and just let it get there." In the 2026-04-04 masterclass this becomes a three-limit ladder (see §2.6). | STATED | oUzc4qeRIhg [34:32] ✔; 787JlWMtCwU [15:09] ✔ |
| 4. Set alerts at the TP levels. If you prefer alerts to limits, set alerts at the entry levels and market-execute when they fire. Never do this on gold. | STATED | 787JlWMtCwU [18:12]-[20:12] ✔ |
| 5. **"Periodically check it over the next couple of days, move your stop loss into break even, then move your stop loss into profit, so it's a risk-free trade, and just let it get there."** | STATED | oUzc4qeRIhg [34:32] ✔ |
| 6. Otherwise live your life. He does not watch the screen: "I'm not stalking the markets 24/7. We trade less, profit more." | STATED | 787JlWMtCwU [15:09] ✔ |
| 7. Monitor, but don't watch every candle. "You monitor it but like you're not thinking of much." | STATED | TaH782wuq7Q [9:13] ✔ |
| Exact check-in times, time zone and review day | NOT STATED | — |

### 2.5 Directional bias: the 3-month rule

| Rule | Label | Source |
|---|---|---|
| **"Look at where you believe price will be 3 months from now, and only trade in that direction."** | STATED | 787JlWMtCwU [8:08] ✔ |
| "If I believe [UJ] is going to get… to… 167, by June or July, every trade I take should only be buys in that direction. There's no need for countertrend trading, no need for selling." | STATED | 787JlWMtCwU [9:08] ✔ |
| "If you believe it's going to be there in 3 months, why is every single trade you take not in that direction?… If you believe it'll be down in 3 months, you're only selling." | STATED | oUzc4qeRIhg [13:19]-[14:19] ✔ |
| In 2025 the same idea was worded per quarter: "where is it going to get to by the end of this quarter… whether it takes two weeks, whether it takes two months." | STATED | TaH782wuq7Q [8:11] ✔ |
| **How he reads the bias:** the weekly A-B-C structure, which shows the D leg ("A, B, C, and then go up to D"), plus the next big psych levels as destinations. | STATED | UXGnJ76wssE [1:04] ✔; 787JlWMtCwU [8:08]-[9:08] |
| **Invalidation: a break in market structure only.** "The only way I will go against it… is if market structure breaks. So the market comes down and then up and then down again, lower high, lower low, boom, lower high, lower low. Then it's like, 'Oh, we're clearly in a downtrend.'" | STATED | oUzc4qeRIhg [32:32] ✔ |
| A pullback that makes a double bottom without a new low leaves the trend intact (UJ, January 2026). | STATED | 787JlWMtCwU [10:08] ✔ |
| Ignore counter-moves on lower timeframes. A big 15m drop can be the "C" leg of a weekly ABC. | STATED | UXGnJ76wssE [1:04]-[2:05] |
| Fundamentals/news as a bias input | NOT STATED in 2025-26. CARRIED OVER: he read TradingView/ForexLive/DailyFX news "for five minutes" (Q6WiIOUcR8k [29:28]) and used DXY for gold (2023-09-23, MEgXUxqSPQ4, [18:12]). | — |
| A pullback against the 3-month direction is a **place to enter**, not a reason to flip. | INFERRED (GA "coming down, it's coming back up, boom" = sell; UJ 61.8 buy) | 787JlWMtCwU [21:13]; UXGnJ76wssE [6:07] |

### 2.6 Entry rules

**E1. Direction filter.** Only enter in the 3-month direction (§2.5). STATED.

**E2. Order type: limits first.**
- "Your entries at least me as a position trader is more predicated on limits" (787JlWMtCwU [14:09] ✔). STATED.
- "I like to place limits so that I'm at least in the trade no matter what. And I just hold them" (787JlWMtCwU [20:12] ✔). STATED.
- Alternative: alerts at the levels, then market-execute. He uses this for USDJPY/GU, because "even if it texts you and you check 5 hours later, sometimes it's not far away." Never for gold (787JlWMtCwU [19:12]-[20:12] ✔). STATED.
- "You probably got to have a balance of limits and alerts. But… I'll just do limits for a lot of the times and I may miss some trades" (787JlWMtCwU [22:14] ✔). STATED.

**E3. The ladder.** STATED.
- When to place it: once the market has made its swing extreme (Fib 0%) and you expect a pullback, "I will get, you know, buy limits around this entire area… one that's like around here, one that's around here, one that's around here" (787JlWMtCwU [15:09] ✔).
- Levels: about the **38.2, 50 and 61.8** retracements (787JlWMtCwU [15:09]-[17:10] ✔).
- Why three: "if the market comes down and wants to go up off the 38.2 or the 50, I'm at least in that trade. Whereas, if you're someone who only gets into the 61.8, you may miss it" (787JlWMtCwU [16:10] ✔).
- Variations: "Some trades I may only do a 61.8 and a 50 and price will get to the 38.2 and go there." Or "I may have my limit right on that third trend line bounce," which may sit at a psych level (787JlWMtCwU [23:14] ✔).
- Confluence: "maximize my confluences with Fibonacci, trend line… extensions or trend line bounces… and factor it all together to get where my entry should be" (787JlWMtCwU [23:14] ✔).
- *VISUAL:* he draws a **purple rectangle as the limit-entry zone**.
  - USDJPY replay: 153.708 → 151.132, i.e. from just under 38.2 to just below 61.8, with arrows marking limits at 38.2, 50 and 61.8.
  - USDCAD: the box spans 50 → 61.8.
  - Actual position-tool entries: USDJPY 152.835 (between 50 and 61.8, at the Jan-26 weekly wick low); GBPAUD ≈ 61.8; USDCAD 1.37835 (= 61.8).
  - The GBPAUD entry also sits on a third touch of a falling trend line.

  Source: (VCN, 787JlWMtCwU 15:20-17:20, 17:40, 21:40; oUzc4qeRIhg 17:40, 32:20).

**E4. Sizing across the ladder.** STATED.
- "The lowest one always has the highest lot size because… you're closer to where your stop loss is… versus 38.2 to your stop loss. So, over here [38.2], I'll get a more conservative… lot size" (787JlWMtCwU [15:09] ✔).
- The exact ratio across 38.2/50/61.8 is **not stated**.
- *CARRIED OVER:* in 2024 the same principle had two orders: "on Market executions I enter with a low lot size… pending orders I… enter with a high lot size" (Q6WiIOUcR8k [13:14]-[14:18]).
- *INFERRED (implementation suggestion only; he gives no formula):* give each order the same dollar risk to the shared stop. Because the 61.8 order sits closest to the stop, it then carries the most lots. This matches his reasoning but is not his stated method.

**E5. No sniper entries, no timing triggers.** STATED.
- "You are no longer looking for sniper entries. Get that out of your mind" (787JlWMtCwU [6:06] ✔).
- "Your entries do not matter when you're position trading… Cuz your stop loss is wide enough" (787JlWMtCwU [14:09] ✔).
- "As a position trader, you're not really worried about your entries" (oUzc4qeRIhg [17:22] ✔).
- **No candle-confirmation trigger** is given for 2026 entries. The limit fills when price gets there.

**E6. Re-entries.** STATED.
- If you don't want to hold one position for a month: "take profit along the way. And then when price gives you a higher low, reenter… comes up, retest the moving average, reenter" (787JlWMtCwU [11:08] ✔).
- *Transitional (early 2025), not repeated in 2026:* a small market order before confirmation, then a buy limit and a buy stop to "trap price," with a 4H candle-close confirmation (2025-03-02, 7YmARnoIJ7I, [1:02]-[5:11]). Treat this as the bridge between his 2024 and 2026 methods, not as a current rule.

**E7. Drawdown is expected after entry.**
- "If you just embrace drawdown just a little bit and was fine with the 20, 30, 40 pips… of a… drawdown… your trading will be a whole lot better" (787JlWMtCwU [23:14] ✔). STATED.

### 2.7 Stop-loss rules

| Rule | Label | Source |
|---|---|---|
| **Placement: "I usually have my stop losses in the middle between the 78.6 and the 100."** Reason: "sometimes it'll get to 78.6 and still go up." | STATED | 787JlWMtCwU [16:10] ✔ |
| **One stop for all ladder entries** ("whether it's a 61.8 or the 50 or a 38.2, you're here. Stop loss is right around in the middle of this"). | STATED | 787JlWMtCwU [17:10] ✔ |
| He adds "Or if you want to get it, you know, lower to the 61.8 or even a 50." The meaning is unclear (see §7). | STATED, unclear | 787JlWMtCwU [17:10] ✔ |
| **On-screen stops are always beyond 78.6% and short of 100%, but not always at the exact midpoint.** USDJPY weekly 148.518 is about a third of the way below 78.6 (midpoint 148.03), a **431.7-pip** stop. USDCAD daily 1.37091 is almost exactly the midpoint, a **74.4-pip** stop. GBPAUD weekly is a **327-pip** stop near the 2.00 psych line. | VISUAL | VCN, 787JlWMtCwU 17:40, 21:40; oUzc4qeRIhg 17:40 |
| **Width is whatever the structure needs:** "You're no longer trying to have a 15 or a 25 pip stop loss… Your stop loss can be as big as you want it to be as long as it gives your trade enough breathing room, it fits the criteria, and your reward is at least three, four, five x that." | STATED | 787JlWMtCwU [6:06] ✔ |
| Typical sizes: "80 pip stop loss, 400 pip TP. Some… 50 pip stop loss, 250 pip TP. Some may be 100 pip stop loss, but a 500 pip TP. It depends on if you're trading USDJPY, gold, or GU, or GA." On a weekly UJ setup: "if this is a 400 stop loss, so what?" | STATED | 787JlWMtCwU [20:12]-[21:13] ✔ |
| Another example: "This is a 80-pip stop loss… We're over a 300-pip TP… 1 and 3.92." | STATED | oUzc4qeRIhg [17:22]-[18:22] ✔ |
| **Size the position to the stop:** "You have to have a stop loss that you're comfortable with in terms of… losing money. So you can't just have a… 10 lot if your stop loss is this wide." | STATED | 787JlWMtCwU [20:12] ✔ |
| The stop and TP are set **before** entry. The trade then "is going to do one of two things. Hit your stop loss or hit your take-profit." | STATED | Short etjvn5pccyM [0:02] ✔ |
| Always use a hard stop sized to a dollar amount you accept losing. | STATED (general) | Short BS6LNqiqXG4 (2025-04-12) [0:02] |
| *Older structural rule, still consistent:* the stop sits beyond the last higher low (long) or lower high (short). If that structure breaks, the idea is wrong. | CARRIED OVER (2023-09-23, MEgXUxqSPQ4, [9:05]; 2020-03-04, -GyagNA9Hdg, [1:02]-[2:03]) | — |

### 2.8 Take-profit rules and partials

| Rule | Label | Source |
|---|---|---|
| **TP ladder:** "TP1 at point zero. TP2 -27 extension. TP3 -61.8. TP4 here [next big psych level, UJ 170]. Now it's a one and four risk-to-reward ratio." | STATED | 787JlWMtCwU [18:12] ✔ |
| He does **not** stop at -27: "I'm not putting my TP as a 27 extension. I'm putting my TP higher… the -61.8. So now it's a one and 3.4 risk-to-reward ratio." | STATED | 787JlWMtCwU [17:10] ✔ |
| **Partials at each TP:** "I will take TPs along the way… take money off the table." The percentage per TP is **not stated** for 2026. | STATED | 787JlWMtCwU [18:12] ✔ |
| In 2025: "Take 10% out, 20, 30, 40% out and still let the trade run." | STATED | TaH782wuq7Q [9:13]-[10:16] ✔ |
| The final target is the **next big psychological level** ("160, 150, 140… 170"). For GA: "come all the way back down to 1.78 before it gets to back to two flat." | STATED | 787JlWMtCwU [18:12], [21:13] ✔ |
| **Minimum reward: 3-5× risk.** Examples: 1:3.4, 1:4 (UJ), 1:5.6 (GA), 1:3.92 (unnamed). | STATED | 787JlWMtCwU [6:06], [17:10]-[21:13]; oUzc4qeRIhg [18:22] |
| **R:R on the position tools:** USDJPY ≈3.4 (TP at -61.8%), then ≈4 when the TP is dragged to 170.048. GBPAUD ≈5.6. USDCAD 3.92 (291.7 / 74.4). His spoken **3-month targets coincide with the Fib extensions**: USDCAD "1.405-1.415" = the -27 / -61.8 extensions (1.40460 / 1.41491). On the weekly, his USDJPY cursor sits at 167.1 on 10 Jul 2026, near the -61.8 extension 167.37. The USDCAD trade uses a single TP at 1.40752, between -27 and -61.8. | VISUAL | VCN, 787JlWMtCwU 8:20-9:50, 17:40-19:40; oUzc4qeRIhg 17:40, 32:20 |
| *Computed geometry (not his statement):* with the stop at the 89.3% retracement (midway between 78.6 and 100), the reward-to-risk to TP3 (-61.8) is about 1:4.5 from a 61.8 fill, 1:2.8 from a 50 fill and 1:2.0 from a 38.2 fill. To TP2 (-27) it is about 1:3.2, 1:2.0 and 1:1.4. Front-loading lots at 61.8 is what pulls the blended R:R toward his quoted 1:3.4 at TP3. | INFERRED (arithmetic) | — |
| *Older habits not repeated in 2026:* take 60-75% off at TP1 (2023-09-23, MEgXUxqSPQ4, [27:18]); close manually when price is a few pips from TP (MEgXUxqSPQ4 [10:05]; Short MyK2U3B7zcI); offset the TP a few pips from the obvious level (Short gvFSTN7JK_c, 2023). | CARRIED OVER, status unknown | — |

### 2.9 Trade management

| Rule | Label | Source |
|---|---|---|
| **Stop to profit after a higher low.** "Price done went up and gave us a [higher] low. So now we can move our stop loss into profit right here… 153 all the way up to 157. Now we are 400 pips in profit, no longer a overall stop loss." | STATED | 787JlWMtCwU [18:12]-[19:12] ✔ |
| "The worst thing that can happen is market comes down and stops you out in profit or it goes all the way back up and hits all your TPs." | STATED | 787JlWMtCwU [19:12] ✔ |
| **Screen vs speech:** on screen he drags the stop to **break-even** (0.001 from entry; the tool shows R:R "17,213"). He does not move it 400 pips above entry. The spoken "400 pips in profit" is the open profit. In practice the first move shown is to break-even. | VISUAL | VCN, 787JlWMtCwU 19:25 |
| Weekly routine version: "move your stop loss into break even, then move your stop loss into profit, so it's a risk-free trade." | STATED | oUzc4qeRIhg [34:32] ✔ |
| *CARRIED OVER (exact trail rule):* move the stop **a few pips beyond** the new higher low (long) or lower high (short). Don't move it before structure forms: "Keep your stop loss in the negatives… until price creates structure." Exception: if you are 40-50 pips up and price starts retracing, move to break-even. | CARRIED OVER (2024-01-01 compilation, mvGXdxGXUu8, [23:23], [63:46]-[64:46]; 2020-07-15, m6XLozeBlzc, [18:22]) | — |
| **Patience:** "What are we being so impatient about? Let the market go." | STATED | 787JlWMtCwU [19:12] ✔ |
| **Do not close early** when your view is unchanged. In a group trade, only about 3 of 100 left it alone and the trade paid. | STATED | Short etjvn5pccyM ✔ |
| **Re-entries** on higher lows or EMA retests after taking profit (E6). | STATED | 787JlWMtCwU [11:08] ✔ |
| **Adding:** several trades in the same direction ("1 2 3 4 5 6 7 trades"). | STATED | 787JlWMtCwU [9:08] ✔ |
| **Weekends / swap:** "We're talking about commissions, rollover fees, swap. Like, pay it. Hold it over the weekend. Pay it." Swap is "like a dollar, two dollars… At the end of a month, you may have paid… 60, 80, 100 dollars… Not a big deal." | STATED | TaH782wuq7Q [15:19] ✔; 787JlWMtCwU [11:08] ✔ |
| **News:** no 2025-26 rule. *CARRIED OVER (2024):* don't open a new trade if major news is due within about 20 minutes. Don't close an open trade for news (CPI/NFP/FOMC) "unless it's completely drastic." | CARRIED OVER (Q6WiIOUcR8k [28:27]-[29:28]) | — |
| **Exit before target:** no 2026 rule beyond the stop or a structure break. *CARRIED OVER:* if structure breaks against you before target, get out (MEgXUxqSPQ4 [25:18]). Cut a trade that "violently turned against you" (2024-08-01, 3EJFLAOsGzg, [27:25]). | CARRIED OVER | — |

### 2.10 Risk management and position sizing

| Rule | Label | Source |
|---|---|---|
| **Risk % per trade in the current system: NOT STATED.** No 2025-26 video gives a % per trade or per idea. | — | — |
| **Every position tool on screen shows "Amount: 750"**: USDJPY (431.7-pip stop), GBPAUD (327-pip stop) and USDCAD (74.4-pip stop). This is consistent with a **fixed $750 risk per trade or per idea, with the lot size adjusted to the stop distance**. He never says it aloud. It may simply be his position-tool default. Account size is unknown, so the % cannot be derived. | VISUAL (not a stated rule) | VCN, 787JlWMtCwU 17:40, 21:40; oUzc4qeRIhg 17:40 |
| How he describes the risk decision: pick a stop distance, then a lot size whose dollar loss you are "comfortable with" (no % given). | STATED | 787JlWMtCwU [20:12] ✔ |
| **Pip-value shorthand he uses:** 1 lot = $10/pip, 2 lots = $20, 3 lots = $30, 5 lots = $50. He applies this to UJ and GA examples too. *Note (not his statement):* on USDJPY and GBPAUD one standard lot is worth roughly $6-7 per pip at 2026 prices, so his dollar figures overstate those pairs. | STATED / note INFERRED | 787JlWMtCwU [10:08]; UXGnJ76wssE [7:07]; oUzc4qeRIhg [4:10] |
| **Lot size matters more than people think:** "the true real reasons are A, your lot sizes are wrong and B, you don't know what you're doing." | STATED | oUzc4qeRIhg [22:25] |
| **Don't yolo:** "putting a crazy high lot size and just guessing." "Don't yolo your trades and try to get a payout day one because you may end up breaching your account." | STATED | 2026-10-22, 5k4JNIHBP_I, [1:05], [8:07] |
| **Prop firms: six-figure accounts only.** "Only do this on a six-figure prop firm account, like a 100K account, 250K account, 500K account." Reason: "if your daily loss on a 10K account is $500, like 5%, you're not going to be doing this because it's easy to lose 500 in a day." | STATED | 787JlWMtCwU [12:08] ✔ |
| On a 500K account: "your daily drawdown is 25K… Your max drawdown is 50K." "Have any of you guys ever lost 50,000 in a month? No." On 100K the drawdown is about $4,000-5,000. "It is much better to take the next month and a half to stack up money and then get a 500K account." | STATED | oUzc4qeRIhg [30:28]-[31:31]; 787JlWMtCwU [13:08] ✔ |
| **Personal brokerage is fine small:** "you can do this with a $5,000 brokerage account" and "$3,000, $4,000, $8,000, $10,000." Plan: "with your first withdrawal… put some of that into your brokerage account so you can scale and position trade on your own." | STATED | 787JlWMtCwU [12:08]-[14:09] ✔ |
| Lot sizes used by traders on his firm's large accounts: "10 lots, 15 lots, 20 lots." "You can use a five lot on… my prop firm." | STATED | UXGnJ76wssE [8:14] ✔ |
| **Return framing:** 10% a month is his benchmark (10% of 500K = $50K). Plan for Q4 2026-Q1 2027: get one or two six-figure accounts, trade them for 3-4 months, be consistent. | STATED | 5k4JNIHBP_I [7:07]-[8:07] |
| **Withdraw rather than compound** (e.g. at +50% on 10K, withdraw about 10% and keep the balance low). | STATED | Short cYn8GKyO48w (2025-08-23) |
| **Judge results quarterly, not monthly.** | STATED | Short W_cn01-q2BY (2025-08-22) |
| His win-rate claims since switching: "10 out of my last 12… 20 out of my last 24… my last 30 out of my last 38." | STATED (unverified) | TaH782wuq7Q [9:13] ✔ |
| *CARRIED OVER (2023), last stated risk band:* "two to four percent is fine, five to eight percent is aggressive… If the trade is amazing I'll even risk five to eight percent, even nine percent, and that's not the norm." 2024: "am I not risking more than 10% more than 5% more than 2%." Whether this still applies to multi-week positions is unknown. | CARRIED OVER (2023-09-10, GgiJOUw7uwk, [28:11]; 2024-08-01, 3EJFLAOsGzg, [23:20]) | — |
| *Unanswered:* how a 3-entry ladder plus "1-7 trades in that direction" is capped in total risk. | NOT STATED | — |

### 2.11 Pre-trade checklist (yes/no)

Built from the rules above. Items marked † are inferred or carried over rather than stated in 2025-26.

1. Have I decided, on the weekly/daily chart, where this instrument is likely to be in about **3 months**? (787JlWMtCwU [8:08])
2. Is this trade **in that direction**, and not counter-trend? (787JlWMtCwU [9:08])
3. Is market structure **intact** in that direction, with no lower-high/lower-low sequence against a long (or the mirror for a short)? (oUzc4qeRIhg [32:32])
4. Is the chart **clean**, not "ugly" or choppy? (UXGnJ76wssE [8:14]; 787JlWMtCwU [25:18])
5. Has the impulse made its swing extreme (Fib **0%**), and is a pullback expected or under way? (787JlWMtCwU [15:09])
6. Is the Fib drawn A (impulse start, 100%) → B (impulse end, 0%) on the weekly/daily swing? † (0z39pJSwy2o; 787JlWMtCwU [8:08])
7. Do my limit levels (≈38.2 / 50 / 61.8) line up with a **psych-level box** and/or a **third trend-line bounce**? (787JlWMtCwU [23:14])
8. Is the **largest lot on the deepest (61.8) limit** and the smallest on 38.2? (787JlWMtCwU [15:09])
9. Is the stop **midway between 78.6 and 100**, shared by all entries? (787JlWMtCwU [16:10])
10. Is the reward to my main target **at least 3× risk** (ideally 4-5×)? (787JlWMtCwU [6:06])
11. Are TP alerts set at **0%, -27, -61.8 and the next big psych level**? (787JlWMtCwU [18:12])
12. Is the total dollar loss at the stop an amount I am **comfortable losing**, and within the account's daily and max loss limits? (787JlWMtCwU [12:08], [20:12]) His on-screen position tools all used a fixed $750 risk. † (VISUAL, VCN)
13. If this is a prop account, is it **six figures**? (787JlWMtCwU [12:08])
14. Is it an **A+ setup**? If not, skip, even if it means no trade this month. (787JlWMtCwU [25:18])
15. Am I prepared to hold through **20-40+ pips of drawdown** and for **days to weeks**? (787JlWMtCwU [23:14]; Short etjvn5pccyM)
16. Is no high-impact news due in the next ~20 minutes if I am entering at market? † (Q6WiIOUcR8k [29:28])

### 2.12 Worked examples of recent trades (2025-2026)

Prices are what he said aloud. Anything only on screen is marked "not stated."

**A. USDJPY long: January → March 2026 (787JlWMtCwU, [9:08]-[11:08])**
- Bias: UJ to 163, then 167 "by June or July", so buys only.
- Entry: the 61.8 retracement in January (price not stated).
- Path: in profit, then "price came back down, double bottom, didn't create a new low, and then it pushed all the way back up 700 pips over a month span."
- Result as he states it: 700 pips. At 3 lots ($30/pip by his shorthand), "$21,000… from simply just holding it."
- Stop: not stated.

**B. USDJPY weekly long with the full ladder (787JlWMtCwU, [15:09]-[20:12])**
- Entries: buy limits at about 38.2 / 50 / 61.8, around 153.
- Stop: midway between 78.6 and 100. About 400 pips ("if this is a 400 stop loss, so what?").
- TPs with alerts:
  - TP1 at Fib 0%
  - TP2 at -27
  - TP3 at -61.8 ("1 and 3.4")
  - TP4 at 170 ("one and four").
- Management: after a higher low he moved the stop to 157. "153 all the way up to 157. Now we are 400 pips in profit."
- Timeline: from about January 26, "a month and a month and a half ago."
- Status at recording: open, stop in profit. (He said "18,000 pip TP"; 153 → 170 is about 1,700 pips, so this is a misspeak.)
- *On screen (VCN, 17:40-19:40):*
  - Fib 146.662 (100%) → 159.458 (0%); -27 = 162.913; -61.8 ≈ 167.37.
  - Long position tool: entry **152.835**, stop **148.518** (431.7 pips), "Amount: 750".
  - Target first at the -61.8 extension (R:R ≈ 3.4), then dragged to **170.048** (1,721.3 pips, R:R ≈ 4).
  - Stop then dragged to break-even.
- A separate live daily long was visible at the start of the video: entry ≈ 158.52, stop 157.508 (just under the 157.5 support box) (VCN, 2:00-2:40).

**C. GBPAUD short: mid-March → about May 2026 (UXGnJ76wssE [6:07]-[8:14]; 787JlWMtCwU [21:13])**
- Called live to his mentorship in mid-March: "GA is coming back up. We need to enter. We should enter right now basically." This means selling the pullback inside a weekly downtrend.
- April view: "the goal is for it to come all the way back down to 1.78 before it gets to back to two flat… a one in 5.6 risk to reward ratio."
- July recap: "The market went from 194 all the way down to 185. That is 900 pips over two months." At a hypothetical 5 lots ($50/pip): "$45,000."
- Target method: "past this psych level and then… down to this psychological level."
- Entry order type and stop: not stated aloud.
- *On screen (VCN, 787JlWMtCwU 21:40):*
  - Weekly Fib 2.01523 (100%) → 1.87058 (0%).
  - Short entry at about the 61.8% (≈1.960), on the third touch of a falling trend line.
  - Stop between 78.6 (1.98428) and 100%, near 2.00: **327 pips**, "Amount: 750".
  - R:R ≈ 5.6, target box toward 1.78.
- These are very likely the same trade.

**D. USDCAD long bias: spring 2026 (oUzc4qeRIhg, [32:32]-[33:32])**
- Bias: by about June, USDCAD "around 141-ish."
- Expected path: "come back down… to test the overall box, come up, boom, higher low, finally break through this trend line."
- Targets: "140,500 or even… 141,500", read as 1.4050 / 1.4150.
- Rule: every trade long. Flip only on lower highs and lower lows.
- Entry and stop: not stated. Result: not reported.

**E. GBPUSD call: December 2025 (oUzc4qeRIhg, [18:22])**
- Called to the group. For 2 days it sat about 30-40 pips in drawdown and people complained. Over the next 3 days it moved "well over 200 250 pips."
- A student passed a prop challenge and got a $15,000 payout.
- Direction implied long. Entry and stop: not stated.

**F. The "80-pip stop" long is USDCAD daily (oUzc4qeRIhg, [17:22]-[18:22]; VCN 17:40-18:20, 32:20-36:20)**
- Spoken: "This is a 80-pip stop loss… We're over a 300-pip TP… 1 and 3.92, basically 1 and 4."
- On screen this is the USDCAD long from example D:
  - Fib 1.36698 (100%) → 1.39660 (0%).
  - Purple entry box 50 → 61.8. Limit entry **1.37835** (= 61.8).
  - Stop **1.37091** (74.4 pips, about the 78.6-100 midpoint). "Amount: 750".
  - Target **1.40752** (~292 pips, between -27 and -61.8). R:R **3.92**.
- The screen therefore shows 74.4 pips, not "80".

**G. Group position trade: about mid-July to late September 2026 (Short etjvn5pccyM, 2026-10-06)**
- Instrument: not named.
- Weeks 1-2: "absolutely nothing." Weeks 3-5: drawdown. He said "just leave it there."
- About 10 weeks in, the target was hit. One member who never touched it was "up… well over $170,000."
- Her lot size, entry, stop and target: not given.

**H. Student's prop-firm run: October 2025 → January 2026 (oUzc4qeRIhg [22:25]-[25:26]; 5k4JNIHBP_I [5:06]-[6:06])**
- About $471K total: +66% on a 500K one-step and +137% on a 100K instant account. Most of it came in about 1.5 weeks in late January 2026, after his guidance.
- Used as a lesson about lot size. Pairs, entries and stops: not given. His figures do not reconcile cleanly (see §6).

**I. Transitional gold long: filmed about late 2024 / early 2025, uploaded 2025-03-02 (7YmARnoIJ7I)**
- Setup: daily uptrend with higher lows; daily Fib A-B-C "right to 61.8"; waited for a 4H candle to close as a doji or small body.
- Orders ("trap price"):
  - 2.5 lots at market
  - a buy limit of 5 lots at 2623, later replaced by 10 lots about "10 pips below price"
  - a buy stop of 10 lots at 2634.
- Target: one target of 2681 for all orders. Maximum loss about $14K vs maximum profit $108K. The starter order was "1 in 5."
- Plan: move the stop to profit after a higher low.
- Result: peaked at about +$40K, then fell back to +$10K. Final result not shown.
- This shows the move to daily-Fib entries but still uses 2024-style lower-timeframe confirmation.

**J. Gold "what-if": the trade that triggered the switch (TaH782wuq7Q, [2:04]-[3:07])**
- "I had a 50 lot… on gold… I was up over $40,000. And my goal was to get it to $108,000." He exited.
- He says gold then "skyrocketed 10,000 pips," and holding would have been "$5 million."
- He links the switch to position trading to this review (also 5k4JNIHBP_I [6:06]: "I missed out on $5 million by simply not holding it").

---

## 3. What he explicitly stopped doing

| Stopped | His words | Source |
|---|---|---|
| **Day trading / screen-glued trading as his main method** | "I'll show you the primary strategy that will work for you in 2026 into 2027 and why other strategies are trash including my former one." "I really was glued to the charts 12 hours a day… I was in Cabo glued to the screen." | oUzc4qeRIhg [0:03]-[1:04], [33:32] |
| | "I used to trade this way. That's why it took me years to get to where I wanted to get to." | UXGnJ76wssE [2:05] |
| | "what I used to do six, seven years ago, wasting my time day trading all day, every day." | Short etjvn5pccyM [1:02] |
| | "I have been trading wrong for the last few years." | TaH782wuq7Q [0:03] |
| **Counter-trend trading** | "There's no need for countertrend trading, no need for selling." | 787JlWMtCwU [9:08] |
| | "back in 2019 and 2020, I'm like, 'Yeah, countertrend trading is I don't believe it anymore.'" | oUzc4qeRIhg [14:19] |
| | Also 2022: "Counter trend trading is very very dangerous." | koKRQ_pPhjQ [15:24] |
| **Tight stops (15-25 pips; earlier 5-10)** | "You're no longer trying to have a 15 or a 25 pip stop loss. Get that out of your mind." | 787JlWMtCwU [6:06] |
| | "I had a 20 pip stop loss. I got in too late. I got in too early." (about half his losses on 81 of 130 trades where his direction was right) | TaH782wuq7Q [7:09]-[8:11] |
| | 2024: "I had the 10 pip stop losses the five pip stop losses" (2014-2015). | WZvdQah_hyI [6:07] |
| **Sniper entries** | "You are no longer looking for sniper entries." | 787JlWMtCwU [6:06] |
| | "I don't care about sniper entries, right, I did in 2020, that's why I made sniper entry videos part one, part two, part three, part four." | 0yoVaP_NTFA [8:11] |
| | "I'm not trying to sniper entry anymore." | 787JlWMtCwU [23:14] |
| **Trading every day / high frequency** | "You're actually a good trader. You're just swinging too many times." "Can you imagine how much simpler life would be if you took 10 trades in three months as opposed to 10 trades in one day?" | TaH782wuq7Q [4:07], [8:11] |
| **Lower-timeframe analysis (1m-15m)** | "go to a five or 15 minute time frame and tell me where the market's going to go. You're going to have a hard time doing that." | UXGnJ76wssE [6:07] |
| **Session-based entries (2023 Asian-session window, never entering in London/NY)** | Not renounced in words. Now "you come in when you want. You take profit when you want," and day trading forces you to "change your schedule to fit the market schedules." | TaH782wuq7Q [18:22] |
| **Closing every Friday / not holding weekends** (his 2020 rule: "I don't hold trades longer than a week") | "Hold it over the weekend. Pay it." | TaH782wuq7Q [15:19] vs 2020-09-19, vHw9Z5q-rqI [6:05] |
| **Taking profit early / closing because of fear** | "I missed out on $5 million by simply not holding it." Check "where it went three weeks later." | 5k4JNIHBP_I [6:06]; UXGnJ76wssE [11:15]; oUzc4qeRIhg [3:08] |
| **Small prop accounts (5K/10K)** | Avoid "10K prop firm account when… the max drawdown is like what? $400?… keep blowing accounts." | oUzc4qeRIhg [30:28]-[31:31] |
| **Old indicators** (RSI, MACD, stochastics: dropped about 2015-16) | "these are the only indicators I use. I don't use RSI." | MEgXUxqSPQ4 [16:11] (2023) |
| **"Old outdated concepts"** (general) | "You guys are taking old outdated concepts and try to apply it to today's market." | 787JlWMtCwU [22:14] |

---

## 4. How the strategy evolved

### 4.1 Timeline table: style, timeframes, holding, sessions, pairs

| Era | Style | Analysis → entry timeframes | Holding period | Frequency | Sessions | Main pairs | Evidence |
|---|---|---|---|---|---|---|---|
| **2015-2017** | Learning; day trader | Obsessed with 1m/5m/15m candles | Intraday | High | — | — | dIhU-khdVYw [6:11] (2021); WZvdQah_hyI [6:07] |
| **2017-2018** | Day trader; discovers psych levels (2017); "a-ha" on risk management (late 2018) | Not stated | Intraday | — | Copied Sean Lee's entry timing | GBPAUD, gold (from Sean Lee's challenge) | qioca4XgFt0 [3:02], [14:08] (2023) |
| **2019** | Day/intraday | — | — | — | Asian into London ("since 2019") | Gold, GBPAUD, AUDUSD | 8ub5s9-Cd-A [2:01]; rejects counter-trend: oUzc4qeRIhg [14:19] |
| **2020** | "Intraday slash swing", level to level | Daily/4H bias → 1H/2H confirmation → **15m/5m sniper entry** | Hours to 2-3 days. **Closes every Friday** ("I don't hold trades longer than a week") | Several a week; "2-3 times" a week preferred over 10-15 | Not fixed; London for GU in one call | Gold, GBPAUD, GBPUSD, AUDUSD/EURUSD | h_WSHrIzSLU; AiFxhnrtHwA; vHw9Z5q-rqI [6:05]; 7OW1HZl08p8 |
| **2021** | Intraday/swing, moving toward fewer, longer trades | 4H/daily for 1-2 week direction → 2H/4H candle confirmation → 15m entry; Fib only on 1H-4H | Wants 1-3 weeks on majors; keeps GA/GJ intraday | "1-2 trades a week" at 8-20 lots | — | AUDUSD, EURUSD, USDCAD, GBPUSD, gold-linked | nOK64T2hLe8 [2:04]-[5:05]; UsbZgSzvpJI [19:16]; 3jF0xjtV6zk [3:05]; dIhU-khdVYw |
| **2022** | Swing | Weekly (last ~12 weeks) → daily/4H/2H (+15m) side by side | Days to weeks | Few positions held ("1 2 3 4 five trades") | — | GBPAUD (favourite), AUDUSD, GBPUSD, gold | koKRQ_pPhjQ (recorded about spring 2022, uploaded 2023-11); 80mLMGmvr2s; dWM8liTEXhA |
| **2023** | Swing with early market entries | Daily/4H/2H; entries timed by session | 1-3 days, up to 7 | 4 core pairs a week; Mon-Wed best | **Enter 6:30/7:30-9:30 pm US Eastern (Asian session)**; "never ever ever enter" London/NY; TP at New York | Gold (favourite), GBPAUD, GBPUSD, AUDUSD, EURJPY | MEgXUxqSPQ4 [4:04]; 0yoVaP_NTFA [7:10], [9:11]; 8ub5s9-Cd-A [2:01] |
| **2024** | Swing ("longer than a day") | Weekly levels → daily → 4H boxes | "A week or two weeks" | "1, 2 or 3 trades every two weeks" | Some Asian-session entries early 2024 | EURUSD, GBPAUD, GBPUSD, USDJPY, gold | WZvdQah_hyI [24:18]-[25:20]; Q6WiIOUcR8k; Short fmr7RJ0gqnM |
| **Early 2025 (transition)** | Daily-based swing/position | Daily Fib → 4H/1H candle confirmation (+15m/5m glance) | Multi-session to days | — | Lets NY session "play out" | Gold | 7YmARnoIJ7I |
| **2025 (from about mid-year)** | **Position trading** | Daily/weekly | Weeks to months ("end of this quarter") | "<10 trades a quarter" | None | Gold (headline), USDJPY | TaH782wuq7Q; Short tXz6sPJASKE |
| **2026** | **Position trading** (3-month bias) | Weekly/daily; Fib and TPs on weekly | 5 days to 2+ months (beginners 8-12 days) | "5-6 a month"; "14 a quarter"; A+ only | None | USDJPY, GBPAUD, GBPUSD, USDCAD; gold only when clean | 787JlWMtCwU; oUzc4qeRIhg; UXGnJ76wssE; Shorts mLT7cdcn5Tg, etjvn5pccyM |

### 4.2 Timeline table: tools, entries, stops, targets, R:R, risk

| Era | Tools | Entries | Stops | Targets | R:R | Risk / size | Evidence |
|---|---|---|---|---|---|---|---|
| **2020** | Round-number key levels and mid-levels as boxes; one or two MAs (8/14 or just 8); Fib 0/38.2/50/61.8/78.6/100, -27/-61.8; candlesticks; consolidation boxes; black charts; alerts | At a level only. Consolidation → 15m break of structure + MA crossover ("sniper"); break-and-retest; MA bounce; 3 confluences minimum | Beyond the last lower high / higher low, a few pips; often ~10-30 pips; "not a fixed 10-20 pips" | Next key level / mid-level; Fib -27 (then -61.8); clone the prior range; trend-line points C→B→A | Min 1:3; examples 1:4 to 1:26 | 1-3% (attribution uncertain); 1 lot ≈ $300 risk; partial 25-50% when up $5-10K; trail by structure | sXKLyERv90c; XiqDimyXScA; 0z39pJSwy2o; DLpx1log7VU; rYF6KfJlUxk; m6XLozeBlzc; jD2zaSD7H-U; zLkMavPyrAg |
| **2021** | **8/14 EMA (entries) + 20/50 EMA (bias)**; Fib on 1H-4H (23.6 removed); quarter levels every 250 pips; 10-11 candle patterns | Candle pattern at level/trend line/Fib, confirmed on 2H/4H → 15m entry; Fib 38.2/50/61.8 with 4-5 touches or a double top/bottom; scale in on pullbacks with fresh 8/14 crosses | Conservative: beyond 78.6. Aggressive: beyond last swing. "No 2-5 pip stops" | -27 extension (hold for -61.8 only on strong momentum); next psych level; prior high | ~2:1 to 3:1 in Fib examples | Not stated; 8-20 lots observed | 3jF0xjtV6zk; UsbZgSzvpJI; dIhU-khdVYw; nOK64T2hLe8 |
| **2022** | Quarters/rays/ellipses; 8/14 EMA (blue/red); **Heikin Ashi**; Fib ext 1.27/1.618/**1.80**; measured moves | After a real retracement, the first engulfing/morning star; sells only when EMAs point down on D/4H/2H | Beyond structure, "room to breathe" | 1.27 (1:3), 1.618 (1:5), 1.80 (1:7); next level | 1:3 to 1:7 | Not stated | koKRQ_pPhjQ; 80mLMGmvr2s |
| **2023** | 8/14 EMA crossover ("only indicators"); psych levels; Heikin Ashi; DXY for gold; TradingView news | **Market-execute early** at 2-3 confluences and accept drawdown; add a ~½-size 2nd entry near the stop; a much bigger 3rd entry after a new LH/HL with the stop moved there; or market + limit | **40-60 pips** beyond structure ("10, 20 pips above" the last lower high) | 180-230 pips; TP1 = 1.27 ext with **60-75% off**; TP2 = 1.618; close when a few pips from TP | 1:3+ ("1:2 if you have to"), 1:4 sweet spot | **2-4% normal, 5-8% aggressive, up to 9%** | MEgXUxqSPQ4; GgiJOUw7uwk; 0yoVaP_NTFA; mvGXdxGXUu8 |
| **2024** | Weekly quarter-level boxes; 4H boxes; Fib; "simple 8 EMA"; candlesticks; trend lines | **Small market order between 38.2 and 50, large limit at 61.8**; 78.6 = "get out" | **40-50 pips** | -27 / -61.8 extension or between; 185-250 pips | 1:3 fixed ("I take every 1:3 setup"); 1:2.8 (market) to 1:8 (limit) | "Not more than 10%… 5%… 2%" | Q6WiIOUcR8k; WZvdQah_hyI; 3EJFLAOsGzg |
| **Early 2025** | Daily Fib ABC; projection tool; counter-trend line; inverse H&S | Small market order before confirmation + buy limit + buy stop ("trap price") after a 4H doji close | ~$8-10 on gold per order | One target (2681) | 1:5 starter; ~1:7.7 overall | ~$14K max loss on ~22.5 lots | 7YmARnoIJ7I |
| **2025-26** | Psych boxes, trend lines, 8/14 EMA, weekly Fib ABC, alerts | **Laddered limits 38.2/50/61.8, biggest at 61.8**; no confirmation trigger | **Midway 78.6-100**; 50-400 pips | **TP1 0%, TP2 -27, TP3 -61.8, TP4 next big psych level**; partials at each | ≥1:3-1:5 (1:3.4, 1:4, 1:5.6 examples) | **Not stated**; six-figure prop accounts; lot size you are "comfortable" losing | 787JlWMtCwU; oUzc4qeRIhg; UXGnJ76wssE; TaH782wuq7Q |

### 4.3 Era notes

**2015-2019 (origins).** He started in 2015 and spent his first years on 1-15 minute charts with 5-10 pip stops and indicators such as RSI and MACD. He discovered psychological levels in 2017 and has called them his core tool ever since. His late-2018 breakthrough was about risk and psychology, not technicals: he studied Sean Lee's 5K→630K challenge, including its pairs (GBPAUD, gold), lot sizes and timing (2023-02-22, qioca4XgFt0). He dates his rejection of counter-trend trading to 2019-2020 (oUzc4qeRIhg [14:19]). No strategy videos from before 2020 were analysed. The only 2018 upload is a Big Brother audition.

**2020 (intraday/swing, level to level).** This is the most-documented era. Levels come first. He waits for consolidation or a candle signal at the level, drops to the 15m or 5m for a "sniper" break-of-structure plus MA-crossover entry, puts a tight structural stop behind it, and targets the next level or the Fib -27 extension, never below 1:3. He trails the stop by structure, scales in at each new lower high or higher low, and closes on Fridays. Even in June 2020 he said he no longer traded the Academy version "structurally and foundationally" (h_WSHrIzSLU [4:05]).

**2021 (fewer, longer trades).** His audit showed "only one or two trades a week" at 8-20 lots, so he started backtesting a 1-3 week hold on majors (nOK64T2hLe8). His teaching videos that year define the tools that still appear today: the 8/14 EMA (with 20/50 for bias), the Fib template without 23.6, and the -27/-61.8 extension targets.

**2022 (swing).** Weekly reading limited to the last ~12 weeks. Side-by-side daily/4H/2H/15m charts. Heikin Ashi added. Extension targets at 1.27/1.618/1.80. "30 minutes a day or less." Strong news filters during the Russia-Ukraine shock.

**2023 (Asian-session swing, 8/14 EMA).** He enters at market in the quiet US-Eastern evening (Asian session), accepts drawdown, scales in, takes 60-75% at TP1, and runs the rest risk-free into New York or for a few days. Stops are 40-60 pips, targets 180-230 pips, risk 2-4% (up to 9%).

**2024 (swing, Fib-based entries).** He says the chart work is unchanged since 2023 and only psychology and execution changed (Q6WiIOUcR8k [3:04]). Entries become a small market order at 38.2-50 plus a large limit at 61.8. Stops are 40-50 pips, holds are 1-2 weeks, and he takes 1-3 trades per fortnight. He launches his prop firm (Nov 2024).

**2025 (switch to position trading).** A transitional gold trade (filmed about late 2024 or early 2025) already uses a daily 61.8 entry but keeps lower-timeframe confirmation. By mid-2025 he says he "developed [it] earlier this year": daily/weekly analysis, "less than 10 trades a quarter," holds for weeks to months, partials of 10-40%, and he pays swap and holds through weekends (TaH782wuq7Q). His stated triggers were (a) seeing what his exited trades would have made if held, (b) 20-pip stops causing about half his losses when his direction was right, and (c) lifestyle.

**2026 (position trading, codified).** In April 2026 he gave the 3-month rule, the limit ladder, the 78.6-100 stop, and the 0/-27/-61.8/psych TP ladder with partials and stop-to-profit after a higher low (787JlWMtCwU, oUzc4qeRIhg). Later 2026 content adds the holding range (5 days to months), frequency (5-6 a month, or 14 a quarter), skipping ugly instruments (gold), and "set it and leave it" (Shorts). He says he is "leaving this industry next year" (787JlWMtCwU [22:14]).

---

## 5. Earlier versions in full

### 5a. The 2020 intraday/swing level-to-level system

**Instruments.** Gold, GBPAUD, GBPUSD, plus AUDUSD (or EURUSD) (2020-02-11, pfoK9v7j7hY, [0:02]). One to three pairs only (XpPde1tTIO0 [19:19]).

**Timeframes.**
- Analyse on the daily/4H. "Look at the daily and the four hour for the overall trend… look at the one-hour, get the confirmation you need and then scale down to the 5 or 15-minute timeframe for your perfect entry" (2020-05-02, AiFxhnrtHwA, [11:15]-[12:16]).
- On the weekly, only the last 2-3 weeks matter (AiFxhnrtHwA [7:10]).
- 4H for "pure structure"; 1H and 15m for entries (2020-06-30, 45UJS0T_dSA, [13:19]).

**Chart.**
- Round-number key levels drawn as thin boxes, with mid-levels between them. Weekly and monthly levels stay on the chart; minor levels are deleted once used (pfoK9v7j7hY [2:02]-[9:06]).
- Quarter-level theory in a lighter form (2020-09-22, DLpx1log7VU, [13:11]).
- One or two MAs: "is it either the 8 and the 14 or the 8" (DLpx1log7VU [5:05]). Type not stated.
- Fib template 0/38.2/50/61.8/78.6/100 with -27 and -61.8 extensions (0z39pJSwy2o [5:09]).
- Trend lines and counter-trend lines; consolidation boxes; black (single-colour) candles (2020-09-15, K3CIP3THGKU, [2:07]); TradingView alerts at levels.

**Entry.**
- Only at a key level, trend line or Fib area: "if we can get in anywhere else, do not even think about getting in" (-GyagNA9Hdg [11:10]).
- At the level: consolidation with many wicks or dojis signals rejection. Draw a box. On the 15m, wait for a break of structure (a lower high or higher low) plus an MA crossover. "Don't wait for the box to break… that's not a sniper entry" (sXKLyERv90c [1:05]-[4:10]).
- Alternatives:
  - break-and-retest of the level (XiqDimyXScA [4:06])
  - MA bounce (ZRMRwGiGkbI [12:11])
  - Fib 38.2/50/61.8 reaction plus a candle (0z39pJSwy2o)
  - counter-trend-line break (DLpx1log7VU [30:25]).
- Minimum three confluences (2020-09-21, rYF6KfJlUxk, [3:04]).
- Trade with the 4H trend: "we don't counter-trend trade at all" (h_WSHrIzSLU [17:17]). Elsewhere he says he has "no bias" at a level and trades whichever way it breaks (XiqDimyXScA [9:14]) — see §6.

**Stop.**
- "If price is going up your stop-loss has to be below the last higher low… if it's going down, above the last lower high" (-GyagNA9Hdg [1:02]).
- Typically about 10 pips on sniper entries (sXKLyERv90c [11:18]), up to about 30 pips (XpPde1tTIO0 [10:13]).
- "Don't listen to people… who say you need a 10 to 20 pip stop loss every time" (DLpx1log7VU [28:25]).

**Targets.**
- "Our take profit level is always the next key level" (-GyagNA9Hdg [19:15]), or the mid-level.
- Fib -27 extension, then -61.8 for scale-ins (0z39pJSwy2o [8:09], [12:13]).
- Cloned range / measured move (K3CIP3THGKU [7:09]); broken trend-line points C→B→A (K3CIP3THGKU [12:14]).
- Never below 1:3 (XiqDimyXScA [9:14]).

**Management.**
- Move the stop to break-even or profit only once structure forms, then trail it behind each new higher low or lower high (m6XLozeBlzc [17:21]-[18:22]; sXKLyERv90c [5:10]-[7:10]).
- Scale in at each new lower high or higher low; all stops move together (XiqDimyXScA [4:06]-[5:07]).
- Partial 25-50% when up $5-10K (m6XLozeBlzc [18:22]).
- Exit by hand when price stalls (dojis plus a lower high) (-GyagNA9Hdg [10:10]) or on a long rejection wick (qGQMJ1R-PTg [27:24]).
- Close everything on Friday and re-enter the next week (vHw9Z5q-rqI [6:05]).

**Risk.**
- "1 to 3%" (2020-06-23, zLkMavPyrAg, [16:50]; speaker attribution uncertain).
- 1 lot with about $300 risk in a live example (jD2zaSD7H-U [7:26]).
- Small accounts: 30-70 pip profits, no big lots (0Al3RzTNJWY).

### 5b. The 2023 Asian-session 8/14 EMA swing system

**Instruments.** Gold ("my favorite pair"), GBPAUD (second), AUDUSD (third), GBPUSD, sometimes EURJPY. Four core pairs on the watch list each week, with 4-5 more used as confluence (CdTM3LGt0dc [1:02], [6:04]; 0yoVaP_NTFA [2:06]). Best days Monday-Wednesday (8ub5s9-Cd-A [2:01]).

**Timeframes.**
- Daily for psych levels and the TP2 view; 4H/2H for DXY and trend lines (MEgXUxqSPQ4 [12:08], [18:12]).
- From the 2022 lessons (published Nov 2023): weekly (last 12 weeks) → daily/4H/2H/15m side by side (koKRQ_pPhjQ).

**Tools.**
- "I got my eight and my 14 crossover two EMAs; these are the only indicators I use" (MEgXUxqSPQ4 [16:11]).
- Psych levels (major whole numbers, mid levels, minor levels) as zones.
- Reaction rays and boxes, trend lines and channels.
- Fib extensions 1.27/1.618 for TP1/TP2. Heikin Ashi for trend.
- Fundamentals: TradingView news and DailyFX, ForexFactory red folders, DXY for gold.

**Session and timing.**
- "I usually enter my trades between 6:30 p.m. and around 9:30 p.m.… like 99% of my trades" (MEgXUxqSPQ4 [4:04]).
- "From between 7:30 and 9:30 at night, sometimes 10:30… Eastern Standard Time" (0yoVaP_NTFA [7:10]).
- "I will never ever ever enter during those times [London/NY]" (MEgXUxqSPQ4 [4:04]).

**Entry.**
- Get in early, at market, once 2-3 confluences agree. Accept drawdown. "I will literally enter… right then right there because I don't want to miss the trade" (0yoVaP_NTFA [2:06]).
- Entry 2: lighter ("half the lot size") at a better level near the stop, after a reversal wick at a psych level, flagged by an alert.
- Entry 3: "way bigger lot size" after a new lower high or higher low, once the stop has moved there (risk-free).
- Alternative: market order plus a limit as the second entry (mvGXdxGXUu8 [40:31]).

**Stop.**
- Beyond structure: "This is the last lower high… that's my stop loss, 10, 20 pips above that" (MEgXUxqSPQ4 [9:05]).
- "I usually have 40 and 50 and 60 because my take profit is so massive" (MEgXUxqSPQ4 [26:18]).

**Targets.**
- 180-230 pips (GgiJOUw7uwk [20:10]).
- TP1 at the 1.27 extension / psych level: take 60-75% off. TP2 at the 1.618 extension.
- "Take profit if it's close to it" (MEgXUxqSPQ4 [10:05]).
- Usually takes profit at the New York session or trails and holds 2-7 days (0yoVaP_NTFA [9:11]).

**Management.**
- Once 90-120 pips up and structure has formed, move the stop to break-even or profit (MEgXUxqSPQ4 [28:18]).
- Exit if structure breaks. Close at TP1 if FOMC or consolidation threatens.

**Risk.**
- 1:3+ ("1:2 if you have to"), 1:4 sweet spot.
- "Two to four percent is fine, five to eight percent is aggressive… even nine percent" (GgiJOUw7uwk [27:10]-[28:11]).
- Raise lot size slowly. Never jump size after a streak.

### 5c. The 2024 swing system

**Style.** "I am also a swing Trader… swing trading doesn't necessarily mean holding for two or three weeks it just means longer than a day" (Q6WiIOUcR8k [6:08], [14:18]). "Hold it for a week or two weeks and then get out." "One two or three trades every two weeks" (WZvdQah_hyI [24:18]-[25:20]).

**Analysis.**
1. Clean chart.
2. Weekly quarter-level key levels, turned into rectangles. Check that price has respected them historically.
3. Trend or range on the weekly/daily.
4. 4H support/resistance boxes.
5. Fib A-B-C on the current swing.
6. Trend lines (don't force them).
7. Candlesticks and the 8 EMA (sometimes 8/16, 20 or 50) as confluence.
8. If-then scenarios.
9. Alerts. "I don't chase the market I let the market come to me" (Q6WiIOUcR8k [2:04]-[19:24]).

Correlations: DXY vs gold; yen futures vs USDJPY.

**Entry.**
- "I usually will Market order somewhere between the 38.2 and the 50 and just be in a little bit of draw down… on Market executions I enter with a low lot size… pending orders I… enter with a high lot size" at the 61.8. "Nine times out of 10 price usually will retrace at the highest point at 61.8" (Q6WiIOUcR8k [13:14]-[15:20]).
- If it reaches 78.6, "we may as well get out the trade."
- No new entries if news is due within 20 minutes.

**Stop.** Above/below the Fib structure. Sizes: "40 and 50 pip stop losses give you the breathing room you need" (WZvdQah_hyI [6:07]).

**Targets.** "TP is right here this 27 or the 61 or right in the middle" (Q6WiIOUcR8k [13:14]). "My take profit is always like 200 Pips 250 225 185… 1 to three to four" (WZvdQah_hyI [6:07]).

**R:R.**
- About 1:2.8-1:3 on the market order and about 1:8 on the 61.8 limit (Q6WiIOUcR8k [13:14]).
- "My risk to reward ratio no matter what is 1 to three if I see a 1 to three setup I'm going to trade it" (3EJFLAOsGzg [11:10]).

**Management.**
- Accept drawdown. Partials at the first target, then hold to the next. Close everything on a W, inverse H&S or morning star against you (Q6WiIOUcR8k [36:28]).
- Don't exit on news unless it is drastic.
- Partial-profit rule from a 2024 Short: never be up 60-70 pips without taking something off; use TP1-TP4 (OmMedf1LWLA).

**Risk.**
- Check the downside: "not risking more than 10% more than 5% more than 2%" (3EJFLAOsGzg [23:20]).
- Win rate "80 or maybe even a 70%" (unclear). January 2024: 31 wins in a row; March 2024: 6 losses in a row (Short W_cn01-q2BY).
- 4 months on, 2 months off; no trading near Christmas (WZvdQah_hyI [8:08]-[9:09]).

---

## 6. Contradictions and inconsistencies

1. **Trade frequency.**
   - "Less than 10 trades a quarter" (TaH782wuq7Q [5:07], Aug 2025).
   - "One or two trades in that direction" per weekly analysis (oUzc4qeRIhg [34:32], Apr 2026).
   - "1 2 3 4 5 6 7 trades in that direction" (787JlWMtCwU [9:08], Apr 2026).
   - "Five trades a month, six trades a month" (UXGnJ76wssE [10:15], Jul 2026), which is 15-18 a quarter.
   - "14 trades in a quarter" (Short mLT7cdcn5Tg, Aug 2026).

   It is also unclear whether one 3-limit ladder counts as one trade or three.
2. **"Set it and don't touch it" vs active management.**
   - The Oct 2026 Short: "We set them before the trade for a reason… just leave it there… I'm not even going to touch it" (etjvn5pccyM).
   - The masterclass: take partials at four TPs and move the stop into profit after a higher low (787JlWMtCwU [18:12]-[19:12]).
   - The weekly routine: move to break-even, then profit, over the next couple of days (oUzc4qeRIhg [34:32]).
3. **When to move to break-even.** 2026: "move your stop loss into break even, then… into profit" during the first couple of days (oUzc4qeRIhg [34:32]). Masterclass: only after a higher low. Older rule: never before structure forms (m6XLozeBlzc [18:22]; mvGXdxGXUu8 [63:46]).
4. **"Entries don't matter" vs a detailed entry ladder.** He says "your entries do not matter when you're position trading" (787JlWMtCwU [14:09]) and in the same video gives exact Fib levels and lot weighting for entries ([15:09]-[16:10]).
5. **Analysis timeframe.** 2025: "doing it on a daily time frame" (TaH782wuq7Q [9:13]). 2026: Fib and TPs on the weekly (787JlWMtCwU [17:10]; UXGnJ76wssE [1:04]). The masterclass also says position trading uses the "daily, weekly" ([2:04]).
6. **Gold focus.** "All you need to focus on is gold" (Short tXz6sPJASKE, Sep 2025). "Shows how much I really focus on UJ versus… gold" (787JlWMtCwU [18:12], Apr 2026). "Gold looks too ugly… I'm not trading it" (UXGnJ76wssE [8:14], Jul 2026).
7. **Account size.** "Only do this on a six-figure prop firm account" vs "you can do this with a $5,000 brokerage account… $3,000, $4,000" (both 787JlWMtCwU [12:08]-[14:09]). The distinction is prop daily-loss limits vs a personal account, but it reads as contradictory.
8. **"The strategy hasn't changed" vs "I've been trading wrong."**
   - "I still trade the exact same way as I traded when I first came in" (qioca4XgFt0 [14:08], 2023).
   - "6 years later, 7 years later I still trade the same way" (mvGXdxGXUu8 [42:32]).
   - "With my strategy nothing has really changed" (Q6WiIOUcR8k [3:04], 2024).
   - Against: "I have been trading wrong for the last few years" (TaH782wuq7Q [0:03]) and "other strategies are trash including my former one" (oUzc4qeRIhg [1:04]).

   Read together, the tools stayed the same and the execution and holding changed.
9. **Counter-trend timing.** He says he stopped counter-trend trading in 2019-2020 (oUzc4qeRIhg [14:19]). Yet in April 2020: "No bias: if market breaks resistance he buys, if it rejects he sells — 'I adapt'" (XiqDimyXScA [9:14]), and in December 2020 "it's okay to be on both sides of the market" (XpPde1tTIO0 [8:13]). In June 2020 he also says "we don't counter-trend trade at all" (h_WSHrIzSLU [17:17]).
10. **Holding weekends.** In 2020 he closed every Friday (vHw9Z5q-rqI [6:05]). In 2021 he closed daily-Fib trades on Friday and re-entered on Monday (3jF0xjtV6zk [4:05]). From 2025 he holds through weekends (TaH782wuq7Q [15:19]).
11. **Order type in practice.** He prefers limits (787JlWMtCwU [14:09], [20:12]). Yet his July 2026 GA call reads as a market entry: "We should enter right now basically" (UXGnJ76wssE [6:07]).
12. **78.6 role.** 2021: the conservative stop goes beyond 78.6 (3jF0xjtV6zk [10:08]). 2024: reaching 78.6 means "we may as well get out" (Q6WiIOUcR8k [13:14]). 2026: the stop goes midway between 78.6 and 100 because price "sometimes… get[s] to 78.6 and still go[es] up" (787JlWMtCwU [16:10]).
13. **R:R claims vs arithmetic.**
    - "1:4" on the 2023 gold example (1943/1961/1900-1910) is really about 1:2 (0yoVaP_NTFA [2:06]).
    - "18,000 pip TP" (787JlWMtCwU [20:12]) vs 153→170 ≈ 1,700 pips.
    - "1 in 17,000" is a joke for "no risk left" ([19:12]).
    - 2024's "40-50 stop, 185-250 target = 1:3-1:4" is really about 1:3.7-1:6 (WZvdQah_hyI [6:07]).
14. **Pip values.** He uses $10/pip per lot for USDJPY and GBPAUD dollar maths (787JlWMtCwU [10:08]; UXGnJ76wssE [7:07]). The true value is lower for those pairs. Gold pip convention: $0.10 = 1 pip ($1 = 10 pips; $10 = 100 pips) (Q6WiIOUcR8k [10:12]; ZRMRwGiGkbI [9:08]). In 7YmARnoIJ7I "10 pips below price" is ambiguous.
15. **The gold trade behind the switch.** "A 50 lot on gold… up over $40,000… goal… $108,000" (TaH782wuq7Q [2:04]-[3:07]). The matching Dubai trade had about 22.5 lots with the same $40K peak and $108K maximum (7YmARnoIJ7I [12:21]-[15:23]).
16. **The student's $471K.** The figures in oUzc4qeRIhg (500K → 834K, then "136-137K" on one account) do not reconcile with 5k4JNIHBP_I (+66% on 500K, +137% on 100K).
17. **Risk %.**
    - 2020: "1 to 3%" (attribution uncertain, zLkMavPyrAg).
    - 2023: "2-4% fine… even 9%," while also saying keep risk "towards the lower… end" (GgiJOUw7uwk [28:11]-[29:13]).
    - 2024: a sliding "10%… 5%… 2%" ceiling.
    - 2025-26: nothing.
18. **2023 entry window.** "6:30… to 9:30 p.m." (MEgXUxqSPQ4 [4:04]) vs "7:30 and 9:30, sometimes 10:30" (0yoVaP_NTFA [7:10]). Also "Asian session going into London… is the main session" (8ub5s9-Cd-A [2:01]) vs "never ever ever enter during [London/NY]."
19. **EMA set.** 2021: 8/14 plus 20/50. 2023: "8 and 14… only indicators." 2024: "usually just a simple 8 EMA" (sometimes 8/16, 20, 50). 2026: "8 and 14 EMA."
20. **Win rate.** A caller said "more than 90%" (UXGnJ76wssE [1:04], not corrected). He claims 30/38 ≈ 79% (TaH782wuq7Q). 2024: "80 or maybe even a 70%." 2023: "you can have a 30% win rate and still be profitable."
21. **Screen vs speech in the April 2026 videos (VCN):**
    - "Move our stop loss into profit… 400 pips in profit": the screen shows the stop dragged to **break-even**.
    - "Middle between the 78.6 and the 100": USDJPY's stop is closer to 78.6 than to the midpoint. USDCAD's is at the midpoint.
    - "80-pip stop": the screen shows 74.4.
    - "Write 160.000" for exact levels: the other lines are placed by hand (155.080, 150.154, 145.046).
    - The replay Fib's 0% is a high that formed **after** some of the replayed bars, so the demo was drawn with hindsight.
    - "23.6 is irrelevant" (2021): 23.6 is on his 2026 template.
    - A fixed "Amount: 750" appears on every position tool and is never mentioned.
22. **Style success-rate statistics** (scalping 1-3%, day 5-10%, swing 15-20%, position 25-30%) are presented as fact with no source ("ask ChatGPT") (787JlWMtCwU [3:05]; UXGnJ76wssE [3:05]).

---

## 7. Open questions / not disclosed

You asked for a 100% replica. **That cannot be built from the public videos.** The items below are missing or ambiguous. Several he explicitly reserves for his paid "Swaggy AI", mentorship or courses: "you can… get an AI… version of me… in case you actually want to ask what are my EMAs and… what colors they should be… and what my Fibonacci settings are" (787JlWMtCwU [7:07]-[8:08]). He also mentions a paid "position" document and a 5-day "position trading intensive" (TaH782wuq7Q).

**Risk and sizing**
1. **Risk % per trade or per idea in the current system.** Not stated. The last stated band is 2023 (2-4%, up to 9%), for a very different style. Visual evidence suggests a fixed **$750** risk on each position tool. Two things are unknown: whether that $750 covers one order or the whole ladder, and what account size it relates to.
2. **Lot split across the 38.2 / 50 / 61.8 limits.** Only "lowest has the highest lot size" and "conservative" at 38.2. No ratio.
3. **Total exposure cap** when running a ladder plus several trades in the same direction ("1-7 trades"), or across correlated pairs (e.g. GBPAUD and GBPUSD). Not stated.
4. **Pip-value convention for non-USD-quoted pairs** in his sizing. His $10/pip shorthand is not literally correct for USDJPY or GBPAUD.

**Fibonacci**

5. **Exact Fib anchoring rule in 2026.** On screen, A=100% sits at the swing low and B=0% at the swing high for longs, on the latest completed daily/weekly impulse, wick to wick as far as 480p shows (VCN). How he decides which impulse qualifies is never stated. The 2020-21 rules (full retracement of about 4-6 candles; start at a confluence) are the best available.
6. **Extension precision.** On screen the template is -61.8 / -27 / 0 / 23.6 / 38.2 / 50 / 61.8 / 78.6 / 100, with no 1.80 or -1.0 (VCN). Whether "-27" is -0.27 or -0.272 cannot be read; the derived prices fit -0.27.
7. **When the ladder is placed.** Immediately after a new swing high? After the first sign of a pullback? On which timeframe's swing (daily or weekly)?
8. **What happens to unfilled limits** if price turns from 38.2 and runs. Are they cancelled at TP1? Moved? Not stated.
9. **The unclear stop sentence:** "Or if you want to get it, you know, lower to the 61.8 or even a 50" (787JlWMtCwU [17:10]). This may mean a tighter stop for shallower entries, or something else.

**Indicators and drawing**

10. **EMA timeframe, colours and current role.** Only "8 and 14 EMA" plus "retest the moving average" for re-entries. On screen there are two MAs (fast blue, slow red/salmon), but the legend is hidden, so the type and periods cannot be confirmed visually (VCN). Whether a crossover still matters is not stated. The 20/50 EMA has not been mentioned since 2021.
11. **Box height for psychological zones** (pips above and below the round number), and **level spacing per pair** in 2026 (UJ was shown every 5.00; others not shown).

**Bias, management and process**

12. **How the 3-month destination is chosen.** Weekly ABC → D projection, next psych level, fundamentals? Only examples are given (UJ 163/167; USDCAD 1.4050/1.4150; GA 1.78).
13. **Partial-profit percentages at TP1-TP4.** Not stated for 2026 (2025: "10, 20, 30, 40%"; 2023: 60-75% at TP1).
14. **Exact trail rule** after the first stop-to-profit move (behind every new higher low? weekly or daily structure?).
15. **News rules for position trades.** Not stated since 2024.
16. **Time zone and timing** of the Sunday/Monday analysis and the "periodic" checks. Not stated. The 2023 session times were US Eastern (0yoVaP_NTFA [7:10]: "Eastern Standard Time"). The 2023-09-23 window (6:30-9:30 pm) does not name a zone but is presumably the same.
17. **Re-entry triggers** in detail (what makes a "higher low" valid; the EMA timeframe for "retest").
18. **Execution platform/broker in 2026.** Not stated.
19. **Instrument list.** No definitive current watch list. Only examples and the "ugly chart" filter.
20. **Results data.** None of the 2025-26 examples gives full entry/stop/exit prices together. Win-rate claims are unverified.

**Chart visuals**

21. **On-screen details.** The two April 2026 videos were reviewed frame by frame (`videos/2026-visual-chart-notes.md`). Their findings are folded into §2 as VISUAL. Remaining limits:
    - The video is 480p, so several labels (61.8, 78.6 and some extension prices) were derived, not read.
    - The MA legend is hidden.
    - Only 3 position tools were visible (USDJPY, GBPAUD, USDCAD).
    - No later 2026 video (UXGnJ76wssE, 5k4JNIHBP_I) was visually reviewed.

---

## 8. Source list (newest first)

### Long videos with write-ups

| Uploaded | ID | Title | Link |
|---|---|---|---|
| 2026-10-22 | 5k4JNIHBP_I | I Built the Prop Firm I Wish Existed Years Ago w/ $2M INSTANT FUNDING... | https://www.youtube.com/watch?v=5k4JNIHBP_I |
| 2026-07-28 | UXGnJ76wssE | In 12 Months, You Will Be Profitable Trader By Doing This... | https://www.youtube.com/watch?v=UXGnJ76wssE |
| 2026-04-04 | 787JlWMtCwU | The EASIEST Way To Profitable Trading For Beginners (Full Video) | https://www.youtube.com/watch?v=787JlWMtCwU |
| 2026-04-03 | oUzc4qeRIhg | Most Trading Strategies Are GARBAGE... Here's One That Actually Works | https://www.youtube.com/watch?v=oUzc4qeRIhg |
| 2025-08-15 | TaH782wuq7Q | I'VE BEEN TRADING WRONG FOR YEARS.... | https://www.youtube.com/watch?v=TaH782wuq7Q |
| 2025-03-02 | 7YmARnoIJ7I | Making $30,000+ In 4 Hours in Dubai With FULL TRADE MANAGEMENT | https://www.youtube.com/watch?v=7YmARnoIJ7I |
| 2024-11-23 | Q6WiIOUcR8k | The Day Trading Forex Strategy That Changed EVERYTHING For Me At 29 (FULL) | https://www.youtube.com/watch?v=Q6WiIOUcR8k |
| 2024-08-01 | 3EJFLAOsGzg | 42 Mins of The BEST PSYCHOLOGY Lessons From All TRADING Books | https://www.youtube.com/watch?v=3EJFLAOsGzg |
| 2024-07-25 | WZvdQah_hyI | 10 Years of Brutal Trading Advice in 47 Mins (NONSTOP HONESTY) | https://www.youtube.com/watch?v=WZvdQah_hyI |
| 2024-01-01 | mvGXdxGXUu8 | 85 MINS OF THE BEST FOREX ADVICE (Trading Study Compilation for 2025) | https://www.youtube.com/watch?v=mvGXdxGXUu8 |
| 2023-12-20 | 0yoVaP_NTFA | I'm a Multi-Millionaire By Following This Exact Schedule... (My Daily Routine) | https://www.youtube.com/watch?v=0yoVaP_NTFA |
| 2023-11-29 | koKRQ_pPhjQ | The Best Technical Analysis Video You'll Ever See On YouTube | https://www.youtube.com/watch?v=koKRQ_pPhjQ |
| 2023-09-23 | MEgXUxqSPQ4 | CHART WORK: The 2023 Strategy That Made Me Over $100K Last Month | https://www.youtube.com/watch?v=MEgXUxqSPQ4 |
| 2023-09-10 | GgiJOUw7uwk | A 30 Minute Risk Management Forex Guide That'll Change Your Life | https://www.youtube.com/watch?v=GgiJOUw7uwk |
| 2023-09-09 | 8ub5s9-Cd-A | Re-Program Your Trading Brain in 17 Minutes… | https://www.youtube.com/watch?v=8ub5s9-Cd-A |
| 2023-09-01 | CdTM3LGt0dc | How I Made $17,000 in 24 Hours (LIVE RESULTS SHOWN) | https://www.youtube.com/watch?v=CdTM3LGt0dc |
| 2023-02-22 | qioca4XgFt0 | when trading finally made sense. a-ha moment revealed | https://www.youtube.com/watch?v=qioca4XgFt0 |
| 2022-04-24 | 80mLMGmvr2s | I May Move to An Island with No Day Trading Taxes... Secure The Swag (Episode 3) | https://www.youtube.com/watch?v=80mLMGmvr2s |
| 2022-02-20 | dWM8liTEXhA | Hitting a 10 Year Goal… Secure The Swag (Episode 2) | https://www.youtube.com/watch?v=dWM8liTEXhA |
| 2021-03-06 | dIhU-khdVYw | An EASY One Hour Japanese Candlestick Guide For Beginners | https://www.youtube.com/watch?v=dIhU-khdVYw |
| 2021-02-22 | UsbZgSzvpJI | 39 Minutes of The Greatest Moving Average Video on YouTube | https://www.youtube.com/watch?v=UsbZgSzvpJI |
| 2021-02-15 | nOK64T2hLe8 | Building a 6 Million Dollar Home & Changing My Forex Day Trading Strategy... (Ep. 5) | https://www.youtube.com/watch?v=nOK64T2hLe8 |
| 2021-02-14 | 3jF0xjtV6zk | A 30 Minute Masterpiece on Trading Fibonacci in Forex | https://www.youtube.com/watch?v=3jF0xjtV6zk |
| 2020-12-12 | XpPde1tTIO0 | How to Trade Support and Resistance in Forex For Beginners | https://www.youtube.com/watch?v=XpPde1tTIO0 |
| 2020-12-06 | TsmCwLPSSws | A Gold Trade, Surprise From My Wife and TJ Making $50m... (Episode 2) | https://www.youtube.com/watch?v=TsmCwLPSSws |
| 2020-11-11 | 7OW1HZl08p8 | The Reality Check All Day Traders Need... | https://www.youtube.com/watch?v=7OW1HZl08p8 |
| 2020-09-22 | DLpx1log7VU | A 48 Minute Guide On EVERYTHING You Need To Know About Technical Analysis | https://www.youtube.com/watch?v=DLpx1log7VU |
| 2020-09-21 | rYF6KfJlUxk | How To Create a Day Trading Plan For Beginners | https://www.youtube.com/watch?v=rYF6KfJlUxk |
| 2020-09-19 | vHw9Z5q-rqI | Scalping, Intraday, and Swing Trading | https://www.youtube.com/watch?v=vHw9Z5q-rqI |
| 2020-09-16 | 0Al3RzTNJWY | The BEST Way For Traders To Grow Their Small Account Quickly | https://www.youtube.com/watch?v=0Al3RzTNJWY |
| 2020-09-15 | K3CIP3THGKU | The Best Way to Trade Trendlines in Forex For Beginners (1-2-3 Strategy) | https://www.youtube.com/watch?v=K3CIP3THGKU |
| 2020-07-29 | qGQMJ1R-PTg | Talking to 2 Millionaires & Buying a Tesla Model X... (Episode 6) | https://www.youtube.com/watch?v=qGQMJ1R-PTg |
| 2020-07-27 | ZRMRwGiGkbI | GOLD MAKES HISTORY!!! WE BROKE $1900/oz | https://www.youtube.com/watch?v=ZRMRwGiGkbI |
| 2020-07-15 | m6XLozeBlzc | Forex Conversations, Praying to God & Talking to Eric Thomas... (Episode 5) | https://www.youtube.com/watch?v=m6XLozeBlzc |
| 2020-07-08 | jD2zaSD7H-U | Live Trading GBP/USD on Instagram Live & Official Apartment Tour... (Episode 4) | https://www.youtube.com/watch?v=jD2zaSD7H-U |
| 2020-06-30 | 45UJS0T_dSA | The Importance of Closing Candlesticks in Forex For Beginners | https://www.youtube.com/watch?v=45UJS0T_dSA |
| 2020-06-23 | h_WSHrIzSLU | My 2020 Day Trading Strategy STEP-BY-STEP | https://www.youtube.com/watch?v=h_WSHrIzSLU |
| 2020-06-23 | zLkMavPyrAg | I Gave $27,000 To My Wife For Her 27th Birthday... (EPISODE 2) | https://www.youtube.com/watch?v=zLkMavPyrAg |
| 2020-05-03 | CiakSkOYh5E | How To Get Sniper Entries in Forex / Part 3 | https://www.youtube.com/watch?v=CiakSkOYh5E |
| 2020-05-02 | AiFxhnrtHwA | The Best Forex TimeFrames For Beginners To Trade On | https://www.youtube.com/watch?v=AiFxhnrtHwA |
| 2020-04-16 | XiqDimyXScA | How To Get Sniper Entries in Trading (Forex For Beginners) | https://www.youtube.com/watch?v=XiqDimyXScA |
| 2020-04-04 | sXKLyERv90c | How I Get Sniper Entries When Trading as a Day Trader | https://www.youtube.com/watch?v=sXKLyERv90c |
| 2020-04-03 | 0z39pJSwy2o | How to Trade With Fibonacci Retracement | https://www.youtube.com/watch?v=0z39pJSwy2o |
| 2020-03-04 | -GyagNA9Hdg | 23 Mins of Value On When To Buy & When To Sell When Trading Forex | https://www.youtube.com/watch?v=-GyagNA9Hdg |
| 2020-02-11 | pfoK9v7j7hY | How to Backtest in Forex So Live Trading Becomes Easier | https://www.youtube.com/watch?v=pfoK9v7j7hY |

### Shorts cited

| Uploaded | ID | Topic | Link |
|---|---|---|---|
| 2026-10-06 | etjvn5pccyM | Position trade held ~10 weeks; big SL/TP set before entry | https://www.youtube.com/shorts/etjvn5pccyM |
| 2026-08-10 | mLT7cdcn5Tg | 14 trades a quarter; not every day is a trading day | https://www.youtube.com/shorts/mLT7cdcn5Tg |
| 2025-09-23 | tXz6sPJASKE | Position-trade gold toward 5,000 | https://www.youtube.com/shorts/tXz6sPJASKE |
| 2025-08-23 | cYn8GKyO48w | Withdraw instead of compounding | https://www.youtube.com/shorts/cYn8GKyO48w |
| 2025-08-22 | W_cn01-q2BY | Judge quarterly; 31/31 and 6-loss streaks (2024) | https://www.youtube.com/shorts/W_cn01-q2BY |
| 2025-04-12 | BS6LNqiqXG4 | Always use a hard stop | https://www.youtube.com/shorts/BS6LNqiqXG4 |
| 2024-08-20 | URNzjwcd6BU | Swing 1-2 weeks; 1-3 trades every two weeks | https://www.youtube.com/shorts/URNzjwcd6BU |
| 2024-08-13 | u1vraMaMgdc | 4 months on, 2 months off | https://www.youtube.com/shorts/u1vraMaMgdc |
| 2024-08-12 | ZpLwTZM5VOo | 40-50 pip stops | https://www.youtube.com/shorts/ZpLwTZM5VOo |
| 2024-05-06 | MuzWLtG8Lk4 | Brokers/platforms in 2024 | https://www.youtube.com/shorts/MuzWLtG8Lk4 |
| 2024-03-03 | MyK2U3B7zcI | Gold long +$40K; close near TP | https://www.youtube.com/shorts/MyK2U3B7zcI |
| 2024-02-19 | OmMedf1LWLA | Partials at 60-70 pips; TP1-TP4 | https://www.youtube.com/shorts/OmMedf1LWLA |
| 2024-02-06 | fmr7RJ0gqnM | Asian-session entries, NY exits (2024 routine) | https://www.youtube.com/shorts/fmr7RJ0gqnM |
| 2023-06-04 | gvFSTN7JK_c | TP offset; early market execution; Heikin Ashi | https://www.youtube.com/shorts/gvFSTN7JK_c |

### Visual review

- `videos/2026-visual-chart-notes.md`: frame-by-frame chart review of 787JlWMtCwU and oUzc4qeRIhg (cited as VCN).

The full Shorts analysis (53 Shorts) is in `shorts/strategy-shorts.md`. The full classification of every channel video is in `VIDEO_INDEX.md`.
