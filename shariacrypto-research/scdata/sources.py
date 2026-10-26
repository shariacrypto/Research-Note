"""Satu fungsi per sumber. Semua mengembalikan dict sederhana atau None bila gagal.
Endpoint gratis:
  DefiLlama   api.llama.fi, stablecoins.llama.fi, coins.llama.fi  (tanpa kunci)
  CoinGecko   api.coingecko.com/api/v3 (Demo key: header x-cg-demo-api-key)
  CMC         pro-api.coinmarketcap.com (Basic key: header X-CMC_PRO_API_KEY)
  Binance     fapi.binance.com (futures), data-api.binance.vision (spot, cadangan)
  DexScreener api.dexscreener.com (tanpa kunci)
  GitHub      api.github.com (GITHUB_TOKEN opsional, menaikkan batas ke 5.000/jam)
"""
from __future__ import annotations
import os, time
from .common import Fetcher, ts_date

LL = "https://api.llama.fi"
CG = "https://api.coingecko.com/api/v3"
CMC = "https://pro-api.coinmarketcap.com"


# ---------------- CoinGecko ----------------
def _cg_headers():
    k = os.getenv("COINGECKO_API_KEY")
    return {"x-cg-demo-api-key": k} if k else {}


def coingecko_coin(f: Fetcher, cg_id: str):
    d = f.get(f"{CG}/coins/{cg_id}", {"localization": "false", "tickers": "false",
              "community_data": "false", "developer_data": "false"},
              _cg_headers(), name=f"cg_coin_{cg_id}")
    if not d:
        return None
    m = d.get("market_data", {})
    u = lambda k: (m.get(k) or {}).get("usd")
    return {"price": u("current_price"), "market_cap": u("market_cap"),
            "fdv": u("fully_diluted_valuation"), "volume_24h": u("total_volume"),
            "circulating": m.get("circulating_supply"), "total": m.get("total_supply"),
            "max": m.get("max_supply"), "ath": u("ath"),
            "ath_date": ((m.get("ath_date") or {}).get("usd") or "")[:10],
            "atl": u("atl"), "atl_date": ((m.get("atl_date") or {}).get("usd") or "")[:10],
            "rank": d.get("market_cap_rank"),
            "updated": (m.get("last_updated") or "")[:16].replace("T", " ")}


def coingecko_chart(f: Fetcher, cg_id: str, days: int = 365):
    """Harga harian 365 hari (batas paket Demo). Kembalikan [(tanggal, harga)]."""
    d = f.get(f"{CG}/coins/{cg_id}/market_chart",
              {"vs_currency": "usd", "days": days, "interval": "daily"},
              _cg_headers(), name=f"cg_chart_{cg_id}")
    if not d or not d.get("prices"):
        return None
    out = {}
    for t, p in d["prices"]:
        out[ts_date(t)] = p  # satu nilai per tanggal (yang terakhir)
    return sorted(out.items())


# ---------------- CoinMarketCap ----------------
def cmc_quote(f: Fetcher, slug: str):
    k = os.getenv("CMC_API_KEY")
    if not k:
        f.log.append({"ok": False, "name": "cmc_quote", "url": CMC,
                      "error": "CMC_API_KEY belum diisi di .env", "optional": True})
        return None
    d = f.get(f"{CMC}/v2/cryptocurrency/quotes/latest", {"slug": slug},
              {"X-CMC_PRO_API_KEY": k}, name=f"cmc_{slug}")
    if not d or not d.get("data"):
        return None
    item = list(d["data"].values())[0]
    if isinstance(item, list):
        item = item[0]
    q = item["quote"]["USD"]
    return {"price": q.get("price"), "market_cap": q.get("market_cap"),
            "fdv": q.get("fully_diluted_market_cap"), "volume_24h": q.get("volume_24h"),
            "circulating": item.get("circulating_supply"), "total": item.get("total_supply"),
            "max": item.get("max_supply"), "rank": item.get("cmc_rank"),
            "updated": (q.get("last_updated") or "")[:16].replace("T", " ")}


# ---------------- DefiLlama ----------------
def llama_price(f: Fetcher, cg_id: str):
    d = f.get(f"https://coins.llama.fi/prices/current/coingecko:{cg_id}", name=f"ll_price_{cg_id}")
    c = (d or {}).get("coins", {}).get(f"coingecko:{cg_id}")
    return c.get("price") if c else None


def llama_chain_tvl(f: Fetcher, chain: str):
    d = f.get(f"{LL}/v2/historicalChainTvl/{chain}", name=f"ll_tvl_{chain}")
    return [(ts_date(x["date"]), x["tvl"]) for x in d] if d else None


def llama_overview(f: Fetcher, kind: str, chain: str, data_type: str | None = None):
    """kind: fees | dexs | derivatives. data_type: dailyFees | dailyRevenue | dailyHoldersRevenue.
    Hasil: total24h/7d/30d, deret harian, dan daftar protokol (nama, kategori, 30h)."""
    p = {"excludeTotalDataChart": "false", "excludeTotalDataChartBreakdown": "true"}
    if data_type:
        p["dataType"] = data_type
    d = f.get(f"{LL}/overview/{kind}/{chain}", p,
              name=f"ll_{kind}_{chain}_{data_type or 'default'}", optional=(kind != "fees"))
    if not d:
        return None
    protos = [{"name": x.get("name"), "slug": x.get("slug"), "category": x.get("category"),
               "d24": x.get("total24h"), "d30": x.get("total30d"),
               "y1": x.get("total1y")} for x in d.get("protocols", [])]
    protos.sort(key=lambda x: -(x["d30"] or 0))
    return {"d24": d.get("total24h"), "d7": d.get("total7d"), "d30": d.get("total30d"),
            "y1": d.get("total1y"),
            "series": [(ts_date(t), v) for t, v in d.get("totalDataChart", [])],
            "protocols": protos}


def llama_summary(f: Fetcher, slug: str, data_type: str = "dailyFees"):
    """Fee/pendapatan satu protokol atau rantai (mis. 'aptos' = gas jaringan)."""
    d = f.get(f"{LL}/summary/fees/{slug}", {"dataType": data_type},
              name=f"ll_summary_{slug}_{data_type}", optional=True)
    if not d:
        return None
    return {"d24": d.get("total24h"), "d7": d.get("total7d"), "d30": d.get("total30d"),
            "y1": d.get("total1y"),
            "series": [(ts_date(t), v) for t, v in d.get("totalDataChart", [])]}


def llama_stablecoins(f: Fetcher, chain: str):
    d = f.get(f"https://stablecoins.llama.fi/stablecoincharts/{chain}",
              name=f"ll_stables_{chain}", optional=True)
    if not d:
        return None
    return [(ts_date(int(x["date"])), (x.get("totalCirculatingUSD") or {}).get("peggedUSD"))
            for x in d]


def llama_chains(f: Fetcher):
    d = f.get(f"{LL}/v2/chains", name="ll_chains", optional=True)
    return {x["name"]: x.get("tvl") for x in d} if d else None


# ---------------- Binance ----------------
def binance_futures(f: Fetcher, symbol: str):
    oi = f.get("https://fapi.binance.com/fapi/v1/openInterest", {"symbol": symbol},
               name=f"bn_oi_{symbol}", optional=True)
    pi = f.get("https://fapi.binance.com/fapi/v1/premiumIndex", {"symbol": symbol},
               name=f"bn_premium_{symbol}", optional=True)
    if not oi and not pi:
        return None
    out = {}
    if oi:
        out["open_interest_token"] = float(oi["openInterest"])
    if pi:
        out["funding_rate"] = float(pi["lastFundingRate"])
        out["mark_price"] = float(pi["markPrice"])
    return out


def binance_weekly(f: Fetcher, symbol: str, limit: int = 60):
    """Cadangan beta: candle mingguan spot. [(tanggal_tutup, close)]"""
    for base in ("https://data-api.binance.vision", "https://api.binance.com"):
        d = f.get(f"{base}/api/v3/klines", {"symbol": symbol, "interval": "1w", "limit": limit},
                  name=f"bn_klines_{symbol}", optional=True)
        if d:
            return [(ts_date(k[6]), float(k[4])) for k in d]
    return None


# ---------------- Dex Screener ----------------
def dexscreener(f: Fetcher, chain: str, token: str):
    d = f.get(f"https://api.dexscreener.com/token-pairs/v1/{chain}/{token}",
              name="dexscreener", optional=True)
    if not d:
        return None
    pairs = sorted(d, key=lambda p: -((p.get("liquidity") or {}).get("usd") or 0))[:10]
    return [{"dex": p.get("dexId"), "pair": f"{p['baseToken']['symbol']}/{p['quoteToken']['symbol']}",
             "liq_usd": (p.get("liquidity") or {}).get("usd"),
             "vol24_usd": (p.get("volume") or {}).get("h24")} for p in pairs]


# ---------------- GitHub ----------------
def github_activity(f: Fetcher, repo: str):
    """Kontributor aktif & commit 52 minggu terakhir di cabang default.
    /stats/contributors menjawab 202 saat GitHub masih menghitung: tunggu lalu ulangi."""
    h = {"Accept": "application/vnd.github+json"}
    if os.getenv("GITHUB_TOKEN"):
        h["Authorization"] = f"Bearer {os.getenv('GITHUB_TOKEN')}"
    url = f"https://api.github.com/repos/{repo}/stats/contributors"
    d = None
    for _ in range(5):
        f.cache.pop(url + "{}", None)
        d = f.get(url, headers=h, name=f"gh_{repo.replace('/', '_')}", optional=True)
        if isinstance(d, list) and d:
            break
        time.sleep(6)
    if not isinstance(d, list) or not d:
        return None
    cutoff = time.time() - 365 * 86400
    active, commits = 0, 0
    for c in d:
        n = sum(w["c"] for w in c.get("weeks", []) if w["w"] >= cutoff)
        commits += n
        active += n > 0
    note = "GitHub hanya mengembalikan 100 kontributor teratas" if len(d) >= 100 else ""
    return {"repo": repo, "kontributor_aktif_12bln": active, "commit_12bln": commits, "catatan": note}
