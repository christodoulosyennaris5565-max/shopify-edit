"""Download spot FX and gold hourly candles from Dukascopy and build daily/weekly bars.

    python duka.py download --out data --symbols USDJPY GBPAUD USDCAD GBPUSD XAUUSD EURUSD AUDUSD
    python duka.py build    --out data

download: fetches BID hourly candles, one file per month, with pauses and retries,
          and skips months already on disk (safe to re-run).
build:    writes data/hourly/<SYM>.csv and data/daily/<SYM>.csv.
          Daily bars use the forex convention: each day closes at 17:00 New York
          (the same daily candles most brokers and TradingView show).

Prices are BID. Spread is added as a cost in the backtest.
"""
import argparse
import lzma
import struct
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

URL = "https://datafeed.dukascopy.com/datafeed/{sym}/{y}/{m:02d}/BID_candles_hour_1.bi5"
URL_DAY = "https://datafeed.dukascopy.com/datafeed/{sym}/{y}/BID_candles_day_1.bi5"
POINT = {"USDJPY": 1e-3, "GBPJPY": 1e-3, "EURJPY": 1e-3, "XAUUSD": 1e-3}
DEFAULT_POINT = 1e-5
FIRST_YEAR = 2014  # he started trading around 2014
NY = ZoneInfo("America/New_York")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def fetch(url, tries=1000):
    wait = 20
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return b""
            print(f"  HTTP {e.code}, waiting {wait}s", flush=True)
        except Exception as e:  # network hiccup
            print(f"  {type(e).__name__}, waiting {wait}s", flush=True)
        time.sleep(wait)
        wait = min(wait * 2, 300)
    raise RuntimeError(f"giving up on {url}")


def decode(blob, month_start, point):
    """bi5 hourly candle = 24 bytes big-endian: seconds, open, close, low, high, volume."""
    if not blob:
        return []
    raw = lzma.decompress(blob)
    rows = []
    for i in range(0, len(raw) - len(raw) % 24, 24):
        t, o, c, lo, hi, v = struct.unpack(">5if", raw[i:i + 24])
        ts = month_start + timedelta(seconds=t)
        rows.append((ts, o * point, hi * point, lo * point, c * point, v))
    return rows


def download(out, symbols, pause):
    now = datetime.now(timezone.utc)
    for sym in symbols:
        d = Path(out) / "raw" / sym
        d.mkdir(parents=True, exist_ok=True)
        point = POINT.get(sym, DEFAULT_POINT)
        for y in range(FIRST_YEAR, now.year + 1):
            for m in range(12):
                if (y, m + 1) >= (now.year, now.month):
                    break  # only completed months
                f = d / f"{y}-{m + 1:02d}.csv"
                if f.exists():
                    continue
                blob = fetch(URL.format(sym=sym, y=y, m=m))
                rows = decode(blob, datetime(y, m + 1, 1, tzinfo=timezone.utc), point)
                with open(f, "w") as fh:
                    fh.write("time_utc,open,high,low,close,volume\n")
                    for r in rows:
                        fh.write(f"{r[0]:%Y-%m-%d %H:%M:%S},{r[1]:.6f},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f},{r[5]:.2f}\n")
                print(f"{sym} {y}-{m + 1:02d}: {len(rows)} bars", flush=True)
                time.sleep(pause)


def download_daily(out, symbols, pause):
    """One file per symbol per year (UTC-midnight daily candles). The current,
    unfinished year comes from monthly hourly files instead."""
    now = datetime.now(timezone.utc)
    for sym in symbols:
        point = POINT.get(sym, DEFAULT_POINT)
        d = Path(out) / "raw_daily" / sym
        d.mkdir(parents=True, exist_ok=True)
        for y in range(FIRST_YEAR, now.year):
            f = d / f"{y}.csv"
            if f.exists():
                continue
            rows = decode(fetch(URL_DAY.format(sym=sym, y=y)), datetime(y, 1, 1, tzinfo=timezone.utc), point)
            _write_rows(f, rows)
            print(f"{sym} {y}: {len(rows)} daily bars", flush=True)
            time.sleep(pause)
        hd = Path(out) / "raw" / sym
        hd.mkdir(parents=True, exist_ok=True)
        for m in range(now.month - 1):
            f = hd / f"{now.year}-{m + 1:02d}.csv"
            if f.exists():
                continue
            rows = decode(fetch(URL.format(sym=sym, y=now.year, m=m)), datetime(now.year, m + 1, 1, tzinfo=timezone.utc), point)
            _write_rows(f, rows)
            print(f"{sym} {now.year}-{m + 1:02d}: {len(rows)} hourly bars", flush=True)
            time.sleep(pause)


def _write_rows(f, rows):
    with open(f, "w") as fh:
        fh.write("time_utc,open,high,low,close,volume\n")
        for r in rows:
            fh.write(f"{r[0]:%Y-%m-%d %H:%M:%S},{r[1]:.6f},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f},{r[5]:.2f}\n")


def build_daily(out):
    """Daily bars from yearly files (UTC days) + current-year hourly (NY-close days).

    Also writes hourly/<SYM>.csv with ONE bar per day, so the engine can run in
    daily-fill mode until real hourly data is available (data/MODE says which).
    """
    out = Path(out)
    for sd in sorted((out / "raw_daily").iterdir()):
        sym = sd.name
        daily = {}
        for f in sorted(sd.glob("*.csv")):
            with open(f) as fh:
                next(fh)
                for line in fh:
                    t, o, h, l, c, v = line.strip().split(",")
                    day = datetime.strptime(t, "%Y-%m-%d %H:%M:%S").date()
                    if day.weekday() >= 5 or float(v) == 0:
                        continue
                    daily[day] = [float(o), float(h), float(l), float(c)]
        for f in sorted((out / "raw" / sym).glob("*.csv")) if (out / "raw" / sym).exists() else []:
            with open(f) as fh:
                next(fh)
                for line in fh:
                    t, o, h, l, c, v = line.strip().split(",")
                    if float(v) == 0:
                        continue
                    ts = datetime.strptime(t, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).astimezone(NY)
                    day = (ts + timedelta(hours=7)).date()
                    if day.weekday() >= 5:
                        continue
                    o, h, l, c = float(o), float(h), float(l), float(c)
                    if day not in daily:
                        daily[day] = [o, h, l, c]
                    else:
                        b = daily[day]
                        b[1], b[2], b[3] = max(b[1], h), min(b[2], l), c
        (out / "daily").mkdir(exist_ok=True)
        (out / "hourly").mkdir(exist_ok=True)
        with open(out / "daily" / f"{sym}.csv", "w") as fd, open(out / "hourly" / f"{sym}.csv", "w") as fhh:
            fd.write("date,open,high,low,close\n")
            fhh.write("time_utc,open,high,low,close\n")
            for day in sorted(daily):
                o, h, l, c = daily[day]
                fd.write(f"{day},{o:.6f},{h:.6f},{l:.6f},{c:.6f}\n")
                fhh.write(f"{day} 12:00:00,{o:.6f},{h:.6f},{l:.6f},{c:.6f}\n")
        (out / "MODE").write_text("daily-fill (one bar per day; same-day ordering is conservative)\n")
        print(f"{sym}: {len(daily)} daily bars ({min(daily)} to {max(daily)})")


def build(out):
    out = Path(out)
    for sd in sorted((out / "raw").iterdir()):
        sym = sd.name
        rows = []
        for f in sorted(sd.glob("*.csv")):
            with open(f) as fh:
                next(fh)
                for line in fh:
                    t, o, h, l, c, v = line.strip().split(",")
                    if float(v) == 0 and float(o) == float(c) == float(h) == float(l):
                        continue  # flat filler bar (market closed)
                    rows.append((t, float(o), float(h), float(l), float(c)))
        if not rows:
            continue
        (out / "hourly").mkdir(exist_ok=True)
        with open(out / "hourly" / f"{sym}.csv", "w") as fh:
            fh.write("time_utc,open,high,low,close\n")
            for r in rows:
                fh.write(f"{r[0]},{r[1]:.6f},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f}\n")
        # daily bars closing 17:00 New York
        daily = {}
        for t, o, h, l, c in rows:
            ts = datetime.strptime(t, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).astimezone(NY)
            day = (ts + timedelta(hours=7)).date()  # 17:00 NY rolls into the next trading day
            if day.weekday() >= 5:
                continue  # weekend slivers
            if day not in daily:
                daily[day] = [o, h, l, c]
            else:
                b = daily[day]
                b[1] = max(b[1], h)
                b[2] = min(b[2], l)
                b[3] = c
        (out / "daily").mkdir(exist_ok=True)
        with open(out / "daily" / f"{sym}.csv", "w") as fh:
            fh.write("date,open,high,low,close\n")
            for day in sorted(daily):
                o, h, l, c = daily[day]
                fh.write(f"{day},{o:.6f},{h:.6f},{l:.6f},{c:.6f}\n")
        print(f"{sym}: {len(rows)} hourly, {len(daily)} daily bars ({min(daily)} to {max(daily)})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["download", "build", "download-daily", "build-daily"])
    ap.add_argument("--out", default="data")
    ap.add_argument("--symbols", nargs="+", default=["USDJPY", "GBPAUD", "USDCAD", "GBPUSD", "XAUUSD", "EURUSD", "AUDUSD"])
    ap.add_argument("--pause", type=float, default=2.0, help="seconds between requests")
    a = ap.parse_args()
    if a.cmd == "download":
        download(a.out, a.symbols, a.pause)
    elif a.cmd == "download-daily":
        download_daily(a.out, a.symbols, a.pause)
    elif a.cmd == "build-daily":
        build_daily(a.out)
    else:
        build(a.out)
