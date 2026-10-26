"""Uji tanpa internet: semua API dipalsukan. Memastikan parser, uji suplai, konflik, beta, dan snapshot berjalan.
    python tests/test_offline.py
Lulus bila tercetak "[scdata] APT: ... metrik" dan checks.md tanpa error. Angka di sini PALSU."""
import sys, math, time, json, random
from pathlib import Path
PKG = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(PKG))
import tempfile
import requests
random.seed(1)
now = time.time(); day = 86400
def daily(n, f): return [[int((now - (n - i) * day) * 1000), f(i)] for i in range(n)]
class Resp:
    def __init__(s, d, code=200): s._d, s.status_code, s.url, s.text = d, code, "mock", json.dumps(d)[:200]
    def json(s): return s._d
def fake(url, params=None, headers=None, timeout=None):
    p = params or {}
    if "coins/aptos/market_chart" in url: return Resp({"prices": daily(366, lambda i: 3.58 * math.exp(-1.46 * i / 365) * (1 + .08 * math.sin(i / 9)))})
    if "coins/bitcoin/market_chart" in url: return Resp({"prices": daily(366, lambda i: 114000 * math.exp(-.32 * i / 365) * (1 + .05 * math.sin(i / 9)))})
    if "api.coingecko.com" in url and "/coins/" in url:
        cid = url.rsplit("/", 1)[1]
        mc = {"aptos": 726e6, "ethereum": 306e9, "solana": 63.5e9, "near": 7e9, "sui": 4.3e9}[cid]
        return Resp({"market_cap_rank": 91, "market_data": {"current_price": {"usd": .8222}, "market_cap": {"usd": mc},
            "fully_diluted_valuation": {"usd": 995e6}, "total_volume": {"usd": 75e6}, "circulating_supply": 883277000,
            "total_supply": 1210000000, "max_supply": None, "ath": {"usd": 19.9}, "ath_date": {"usd": "2023-01-30T00:00Z"},
            "atl": {"usd": .5129}, "atl_date": {"usd": "2026-08-30T00:00Z"}, "last_updated": "2026-10-22T01:30:00Z"}})
    if "coinmarketcap" in url:
        return Resp({"data": {"21794": {"circulating_supply": 883280000, "total_supply": 1210000000, "max_supply": 2100000000, "cmc_rank": 75,
            "quote": {"USD": {"price": .8415, "market_cap": 743.32e6, "fully_diluted_market_cap": 1.76e9, "volume_24h": 99e6, "last_updated": "2026-10-22T01:30:00Z"}}}}})
    if "//coins.llama.fi" in url: return Resp({"coins": {"coingecko:aptos": {"price": .823}}})
    if "historicalChainTvl" in url: return Resp([{"date": int(now - (500 - i) * day), "tvl": 1e9 - i * 1e6} for i in range(500)])
    if "/overview/fees/" in url:
        return Resp({"total24h": 5e4, "total7d": 3.5e5, "total30d": 1.42e6, "total1y": 1.5e7,
            "totalDataChart": [[int(now - (500 - i) * day), 4e4 + i * 20] for i in range(500)],
            "protocols": [{"name": "Securitize", "slug": "securitize", "category": "RWA", "total30d": 623e3},
                          {"name": "Decibel", "slug": "decibel", "category": "Derivatives", "total30d": 559e3},
                          {"name": "Aptos", "slug": "aptos", "category": "Chain", "total30d": 141e3},
                          {"name": "Echelon", "slug": "echelon", "category": "Lending", "total30d": 64e3},
                          {"name": "Thala", "slug": "thala", "category": "Dexs", "total30d": 32e3},
                          {"name": "Foo", "slug": "foo", "category": "Yield", "total30d": 5e3}]})
    if "/overview/dexs/" in url or "/overview/derivatives/" in url:
        return Resp({"total24h": 1e7, "total30d": 3e8, "totalDataChart": [[int(now - (500 - i) * day), 1e7] for i in range(500)], "protocols": []})
    if "/summary/fees/" in url:
        k = p.get("dataType")
        base = {"dailyFees": 4700, "dailyRevenue": 4700, "dailyHoldersRevenue": 4700}[k]
        return Resp({"total24h": base, "total7d": base * 7, "total30d": base * 30, "total1y": base * 200,
                     "totalDataChart": [[int(now - (500 - i) * day), base * (0.3 if i < 290 else 1.0)] for i in range(500)]})
    if "stablecoincharts" in url: return Resp([{"date": str(int(now - (500 - i) * day)), "totalCirculatingUSD": {"peggedUSD": 1.2e9}} for i in range(500)])
    if "fapi.binance.com" in url and "openInterest" in url: return Resp({"openInterest": "40000000"})
    if "premiumIndex" in url: return Resp({"lastFundingRate": "0.0001", "markPrice": "0.822"})
    if "dexscreener" in url: return Resp([{"dexId": "thala", "baseToken": {"symbol": "APT"}, "quoteToken": {"symbol": "USDC"}, "liquidity": {"usd": 5e6}, "volume": {"h24": 2e6}}])
    if "api.github.com" in url:
        return Resp([{"weeks": [{"w": int(now - k * 7 * day), "c": (1 if j % 3 else 0)} for k in range(60)]} for j in range(120)])
    return Resp({"err": "unknown"}, 404)
requests.get = fake
import scdata.fetch as F
out = F.run(str(PKG / "assets/APT.json"), out_root=Path(tempfile.mkdtemp()))
print((out / "checks.md").read_text())
s = json.loads((out / "summary.json").read_text())
print(json.dumps({k: s[k] for k in ["beta", "tren_pendapatan", "penggunaan_12bln_pct"]}, indent=1))
print(s["fee_per_aplikasi"]["porsi_pct"], s["pembanding"][0])
print(open(next(out.glob("snapshot_*.csv"))).read()[:1500])
