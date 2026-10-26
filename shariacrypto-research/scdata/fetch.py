"""Ambil semua data satu aset → data/out/<TICKER>_<tgl>/
    python -m scdata.fetch assets/APT.json            # run penuh
    python -m scdata.fetch assets/APT.json --no-peers # tanpa pembanding (lebih cepat)
Keluaran:
    snapshot_<TICKER>_<tgl>.csv  format PANDUAN §8.1 (siap unggah ke Drive)
    summary.json                 ringkasan padat untuk dibaca Claude (hemat token)
    checks.md                    hasil uji identitas suplai + konflik + kegagalan sumber
    series/*.csv                 deret waktu untuk grafik
    raw/*.json                   respons mentah (audit; jangan dibaca utuh oleh Claude)
    fetch_log.txt                OK / GAGAL / SKIP per endpoint
Kode keluar 0 = selesai (walau ada sumber opsional gagal); 2 = data inti (harga/suplai) gagal.
"""
from __future__ import annotations
import argparse, json, sys, datetime as dt
from pathlib import Path
from .common import ROOT, Fetcher, Snapshot, load_env, now_wib, write_series
from . import sources as S, checks as C


def run(cfg_path: str, peers: bool = True, out_root: Path = ROOT / "data" / "out") -> Path:
    load_env()
    cfg = json.loads(Path(cfg_path).read_text(encoding="utf-8"))
    tk, today = cfg["ticker"], dt.date.today().isoformat()
    out = out_root / f"{tk}_{today}"
    out.mkdir(parents=True, exist_ok=True)
    f, snap, t = Fetcher(out), Snapshot(), now_wib()
    summ: dict = {"ticker": tk, "nama": cfg.get("nama"), "waktu_ambil": t, "flags": []}

    # 1) Harga, MC, suplai: CoinGecko + CMC + DefiLlama (cek silang)
    cg = S.coingecko_coin(f, cfg["coingecko_id"])
    cm = S.cmc_quote(f, cfg.get("cmc_slug", cfg["coingecko_id"]))
    llp = S.llama_price(f, cfg["coingecko_id"])
    if cg:
        w = cg["updated"] or t
        for k, sat in [("price", "USD"), ("market_cap", "USD"), ("fdv", "USD"),
                       ("volume_24h", "USD"), ("circulating", tk), ("total", tk),
                       ("max", tk), ("ath", "USD"), ("atl", "USD"), ("rank", "peringkat")]:
            snap.add(f"cg_{k}", cg[k], sat, f"CoinGecko API coins/{cfg['coingecko_id']}", w)
    if cm:
        for k, sat in [("price", "USD"), ("market_cap", "USD"), ("fdv", "USD"),
                       ("volume_24h", "USD"), ("circulating", tk), ("total", tk),
                       ("max", tk), ("rank", "peringkat")]:
            snap.add(f"cmc_{k}", cm[k], sat, "CoinMarketCap API v2 quotes/latest", cm["updated"] or t)
    snap.add("llama_price", llp, "USD", "DefiLlama coins API", t)
    base = cg or cm
    if not base:
        summ["flags"].append("FATAL: harga & suplai gagal diambil dari CoinGecko dan CMC")
    summ["pasar"] = {"coingecko": cg, "cmc": cm, "defillama_price": llp}

    # 2) Identitas suplai
    sm = cfg.get("suplai_manual", {})
    comps = sm.get("komponen", {})
    for k, v in comps.items():
        snap.add(f"suplai_{k}", v[0], tk, f"manual: {v[1]}", sm.get("waktu", "lihat sumber"))
    if sm.get("batas_maks"):
        snap.add("batas_maks_resmi", sm["batas_maks"][0], tk, f"manual: {sm['batas_maks'][1]}",
                 sm.get("waktu", ""))
    if base:
        maxs = (sm.get("batas_maks") or [None])[0] or base.get("max")
        summ["uji_suplai"] = C.supply_identity(base["circulating"], base["total"], maxs, comps)
        if not summ["uji_suplai"]["lulus"]:
            summ["flags"].append("UJI SUPLAI GAGAL: lihat checks.md sebelum menulis bagian suplai/unlock")

    # 3) Konflik antar sumber
    pairs = []
    if cg and cm:
        for m, k in [("harga", "price"), ("market_cap", "market_cap"), ("volume_24h", "volume_24h"),
                     ("suplai_beredar", "circulating"), ("suplai_total", "total")]:
            pairs.append((m, cg[k], "CoinGecko", cm[k], "CMC"))
    if cg and llp:
        pairs.append(("harga_vs_defillama", cg["price"], "CoinGecko", llp, "DefiLlama"))
    summ["konflik"] = C.conflicts(pairs)
    if summ["konflik"]:
        summ["flags"].append(f"{len(summ['konflik'])} konflik antar sumber perlu rekonsiliasi")

    # 4) Beta 52 minggu vs BTC (CoinGecko harian → mingguan; cadangan Binance mingguan)
    a = S.coingecko_chart(f, cfg["coingecko_id"])
    b = S.coingecko_chart(f, "bitcoin")
    src = "CoinGecko harian, diambil tiap 7 hari"
    if a and b:
        aw, bw = C.to_weekly(a), C.to_weekly(b)
        write_series(out, "harga_harian", [(d, p) for d, p in a], ("tanggal", "harga_usd"))
        write_series(out, "btc_harian", b, ("tanggal", "harga_usd"))
    else:
        aw = S.binance_weekly(f, cfg.get("binance_symbol", f"{tk}USDT"))
        bw = S.binance_weekly(f, "BTCUSDT")
        src = "Binance spot mingguan"
    be = C.beta(aw, bw) if aw and bw else None
    if be:
        be["sumber"] = src
        summ["beta"] = be
        snap.add("beta_52mgg_vs_BTC", be["beta"], "rasio", f"hitungan sendiri regresi log-return mingguan ({src}); korelasi {be['korelasi']}", be["sampai"])
        snap.add("return_52mgg", be["return_asset_pct"], "%", f"hitungan sendiri ({src})", be["sampai"])
        snap.add("return_52mgg_BTC", be["return_btc_pct"], "%", f"hitungan sendiri ({src})", be["sampai"])
        snap.add("volatilitas_tahunan", be["vol_tahunan_pct"], "%", f"hitungan sendiri ({src})", be["sampai"])
        write_series(out, "indeks_vs_btc", [(d, x / aw[0][1] * 100, y / bw[0][1] * 100)
                     for d, x, y in C.align(aw, bw)], ("tanggal", tk, "BTC"))
    else:
        summ["flags"].append("Beta tidak bisa dihitung (deret harga gagal); pakai Yahoo manual")

    # 5) DefiLlama: TVL, fee, pendapatan, DEX, perp, stablecoin
    ll = cfg.get("defillama", {})
    chain = ll.get("chain")
    usage = {}
    if chain:
        tvl = S.llama_chain_tvl(f, chain)
        if tvl:
            write_series(out, "tvl", tvl, ("tanggal", "tvl_usd"))
            snap.add("tvl_rantai", tvl[-1][1], "USD", f"DefiLlama historicalChainTvl/{chain}", tvl[-1][0])
            usage["tvl_12bln_pct"] = C.change_12m(tvl)
        apps = S.llama_overview(f, "fees", chain, "dailyFees")
        if apps:
            write_series(out, "fee_aplikasi_harian", apps["series"], ("tanggal", "fee_usd"))
            snap.add("fee_aplikasi_30h", apps["d30"], "USD", f"DefiLlama overview/fees/{chain}", t)
            summ["fee_per_aplikasi"] = C.app_fee_shares(
                apps["protocols"], cfg.get("syariah_kategori", {}), cfg.get("syariah_override", {}))
            for k, v in summ["fee_per_aplikasi"]["porsi_pct"].items():
                snap.add(f"porsi_fee_aplikasi_{k}", v, "%", "DefiLlama overview/fees + klasifikasi Shariacrypto (config)", t)
            usage["fee_aplikasi_12bln_pct"] = C.change_12m(apps["series"])
        hrev = S.llama_overview(f, "fees", chain, "dailyHoldersRevenue")
        if hrev:
            snap.add("holders_revenue_aplikasi_30h", hrev["d30"], "USD", f"DefiLlama overview/fees/{chain} dailyHoldersRevenue", t)
        for kind in ("dexs", "derivatives"):
            o = S.llama_overview(f, kind, chain)
            if o:
                snap.add(f"volume_{kind}_30h", o["d30"], "USD", f"DefiLlama overview/{kind}/{chain}", t)
                write_series(out, f"volume_{kind}", o["series"], ("tanggal", "volume_usd"))
                usage[f"volume_{kind}_12bln_pct"] = C.change_12m(o["series"])
        stb = S.llama_stablecoins(f, chain)
        if stb:
            write_series(out, "stablecoin", stb, ("tanggal", "usd"))
            snap.add("stablecoin_beredar", stb[-1][1], "USD", f"DefiLlama stablecoincharts/{chain}", stb[-1][0])
            usage["stablecoin_12bln_pct"] = C.change_12m(stb)

    # Pendapatan token/protokol sendiri (gas rantai atau protokol)
    slug = ll.get("fees_slug")
    if slug:
        fees = S.llama_summary(f, slug, "dailyFees")
        rev = S.llama_summary(f, slug, "dailyRevenue")
        hold = S.llama_summary(f, slug, "dailyHoldersRevenue")
        for lab, d in [("fee", fees), ("pendapatan", rev), ("pendapatan_holder", hold)]:
            if not d:
                continue
            snap.add(f"{lab}_24j", d["d24"], "USD", f"DefiLlama summary/fees/{slug}", t)
            snap.add(f"{lab}_30h", d["d30"], "USD", f"DefiLlama summary/fees/{slug}", t)
            if d["d30"]:
                snap.add(f"{lab}_disetahunkan_30h", d["d30"] * 365 / 30, "USD", "hitungan sendiri 30h×365/30 (est.)", t)
            snap.add(f"{lab}_1thn", d["y1"], "USD", f"DefiLlama summary/fees/{slug} total1y", t)
            write_series(out, f"{lab}_harian", d["series"], ("tanggal", "usd"))
        main = rev or fees
        if main:
            summ["tren_pendapatan"] = C.revenue_trend(main["series"])
            summ["stabilitas_pendapatan"] = C.monthly_cv(main["series"])
            usage["fee_token_12bln_pct"] = C.change_12m((fees or main)["series"])
            if summ["tren_pendapatan"]:
                snap.add("tren_pendapatan_kuartal_x4_vs_12bln", summ["tren_pendapatan"]["perubahan_pct"], "%", "hitungan sendiri DefiLlama", t)
            if summ["stabilitas_pendapatan"]:
                snap.add("cv_pendapatan_bulanan", summ["stabilitas_pendapatan"]["cv"], "rasio", "hitungan sendiri DefiLlama 12 bln", t)
    summ["penggunaan_12bln_pct"] = usage

    # 6) Derivatif Binance, DEX Screener, GitHub
    bn = S.binance_futures(f, cfg.get("binance_symbol", f"{tk}USDT"))
    if bn:
        summ["binance"] = bn
        if base and bn.get("open_interest_token"):
            oi_usd = bn["open_interest_token"] * (bn.get("mark_price") or base["price"])
            snap.add("open_interest_binance", oi_usd, "USD", "Binance fapi openInterest × markPrice", t)
            snap.add("oi_binance_per_mc", oi_usd / base["market_cap"] * 100, "%", "hitungan sendiri", t)
        snap.add("funding_rate_binance", bn.get("funding_rate"), "per 8 jam", "Binance fapi premiumIndex", t)
    ds = cfg.get("dexscreener")
    if ds:
        summ["dex_pairs"] = S.dexscreener(f, ds["chain"], ds["token"])
    gh = [g for g in (S.github_activity(f, r) for r in cfg.get("github", [])) if g]
    if gh:
        summ["github"] = gh
        snap.add("kontributor_aktif_12bln", sum(g["kontributor_aktif_12bln"] for g in gh), "orang",
                 "GitHub stats/contributors " + ", ".join(g["repo"] for g in gh), t)
        snap.add("commit_12bln", sum(g["commit_12bln"] for g in gh), "commit", "GitHub stats/contributors", t)

    # 7) Pembanding (valuasi): MC, FDV, fee, pendapatan holder
    if peers:
        rows = []
        for p in cfg.get("pembanding", []):
            pc = S.coingecko_coin(f, p["coingecko_id"])
            pf = S.llama_summary(f, p["fees_slug"], "dailyFees") if p.get("fees_slug") else None
            ph = S.llama_summary(f, p["fees_slug"], "dailyHoldersRevenue") if p.get("fees_slug") else None
            r = {"ticker": p["ticker"], "mc": pc and pc["market_cap"], "fdv": pc and pc["fdv"],
                 "fee_30h": pf and pf["d30"], "holder_rev_30h": ph and ph["d30"]}
            if r["mc"] and r["holder_rev_30h"]:
                r["mc_per_holder_rev_thn"] = round(r["mc"] / (r["holder_rev_30h"] * 365 / 30), 1)
            rows.append(r)
            for k in ("mc", "fdv", "fee_30h", "holder_rev_30h"):
                snap.add(f"pembanding_{p['ticker']}_{k}", r[k], "USD", "CoinGecko / DefiLlama", t)
        summ["pembanding"] = rows

    # 8) Tulis keluaran
    snap.write(out / f"snapshot_{tk}_{today}.csv")
    f.write_log()
    gagal = [e for e in f.log if not e["ok"] and not e.get("optional")]
    summ["sumber_gagal"] = [f"{e['name']}: {e['error']}" for e in gagal]
    summ["sumber_opsional_gagal"] = [e["name"] for e in f.log if not e["ok"] and e.get("optional")]
    (out / "summary.json").write_text(json.dumps(summ, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    write_checks_md(out, summ)
    print(f"[scdata] {tk}: {len(snap.rows)} metrik → {out}")
    for fl in summ["flags"]:
        print("  !", fl)
    if not base:
        sys.exit(2)
    return out


def write_checks_md(out: Path, s: dict):
    L = [f"# Uji data {s['ticker']} — {s['waktu_ambil']}", ""]
    u = s.get("uji_suplai")
    if u:
        L += [f"## Identitas suplai: {'LULUS' if u['lulus'] else 'GAGAL'}",
              f"- Tidak beredar (total − beredar): {u.get('tidak_beredar', 0):,.0f}",
              f"- Jumlah komponen di config: {u.get('jumlah_komponen', 0):,.0f}",
              f"- Sisa: {u.get('sisa', 0):,.0f} ({u.get('sisa_pct_total', 0)}% total)"]
        L += [f"- {x}" for x in u["temuan"]] + [""]
    L.append("## Konflik antar sumber")
    L += [f"- {c['metrik']}: {c['sumber_a']} {c['a']:,} vs {c['sumber_b']} {c['b']:,} "
          f"(selisih {c['selisih_pct']}%) → {c['tindakan']}" for c in s.get("konflik", [])] or ["- tidak ada"]
    L += ["", "## Sumber gagal (wajib dicatat di Doc arsip)"]
    L += [f"- {x}" for x in s.get("sumber_gagal", [])] or ["- tidak ada"]
    L += [f"- (opsional) {x}" for x in s.get("sumber_opsional_gagal", [])]
    L += ["", "## Bendera"] + ([f"- {x}" for x in s["flags"]] or ["- tidak ada"])
    (out / "checks.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--no-peers", action="store_true")
    a = ap.parse_args()
    run(a.config, peers=not a.no_peers)
