# -*- coding: utf-8 -*-
"""
Ambil logo koin dari sumber terbuka lalu simpan sebagai data URI untuk Research Note.

Usage:
    python3 rn_logo.py TICKER [--tw JALUR_TRUSTWALLET] [--sym SIMBOL] [--url URL]

Contoh:
    python3 rn_logo.py BTC --tw blockchains/bitcoin/info
    python3 rn_logo.py ETH --tw blockchains/ethereum/info
    python3 rn_logo.py GEOD --tw blockchains/solana/assets/<mint_address>
    python3 rn_logo.py DOGE --sym doge

Urutan sumber (berhenti di yang pertama berhasil):
  1. --url (bila diberikan; harus PNG/SVG/JPEG langsung)
  2. Trust Wallet Assets (MIT)   raw.githubusercontent.com/trustwallet/assets/master/<tw>/logo.png
  3. spothq/cryptocurrency-icons (CC0)  .../svg/color/<sym>.svg
  4. ErikThiart/cryptocurrency-icons     .../128/<sym>.png
Hasil: logo_<TICKER>.txt (data URI, dipakai di exec.logo_file) dan logo_<TICKER>.png/.svg untuk dicek visual.
Wajib: buka PNG hasilnya dan pastikan logonya benar (bukan token lain dengan ticker sama).
Bila semua gagal: jangan isi logo; builder memakai lencana ticker (isi exec.ticker).
"""
import base64, subprocess, sys

RAW = 'https://raw.githubusercontent.com'


def fetch(url):
    r = subprocess.run(['curl', '-sfL', '-m', '20', url], capture_output=True)
    return r.stdout if r.returncode == 0 and len(r.stdout) > 200 else None


def main():
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    tk = a[0].upper()
    opt = {a[i]: a[i + 1] for i in range(1, len(a) - 1, 2)}
    sym = opt.get('--sym', tk.lower())
    cands = []
    if '--url' in opt:
        cands.append(opt['--url'])
    if '--tw' in opt:
        cands.append(f"{RAW}/trustwallet/assets/master/{opt['--tw'].strip('/')}/logo.png")
    cands += [f'{RAW}/spothq/cryptocurrency-icons/master/svg/color/{sym}.svg',
              f'{RAW}/ErikThiart/cryptocurrency-icons/master/128/{sym}.png']
    for u in cands:
        b = fetch(u)
        if not b:
            print('gagal :', u)
            continue
        if b.lstrip()[:5] in (b'<?xml', b'<svg ') or b'<svg' in b[:300]:
            mime, ext = 'image/svg+xml', 'svg'
        elif b[:8] == b'\x89PNG\r\n\x1a\n':
            mime, ext = 'image/png', 'png'
        elif b[:3] == b'\xff\xd8\xff':
            mime, ext = 'image/jpeg', 'jpg'
        else:
            print('bukan gambar:', u)
            continue
        if len(b) > 80_000:
            print('terlalu besar (>80 KB), lewati:', u)
            continue
        open(f'logo_{tk}.{ext}', 'wb').write(b)
        open(f'logo_{tk}.txt', 'w').write(f'data:{mime};base64,' + base64.b64encode(b).decode())
        print(f'OK  : {u}\n      -> logo_{tk}.txt ({len(b)} byte). Cek visual logo_{tk}.{ext} sebelum dipakai.')
        print(f'      Sumber untuk Bagian 8: {u.split("/")[3]}/{u.split("/")[4]}')
        return
    print('Semua sumber gagal: pakai lencana ticker (exec.ticker) dan catat di asumsi run.')
    sys.exit(1)


if __name__ == '__main__':
    main()
