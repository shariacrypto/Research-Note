import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, datetime as dt
from matplotlib import font_manager as fm
plt.rcParams.update({'font.family':'Inter','font.size':10})
BG='#072E1A'; GRID='#1E4A2A'; TXT='#E8F0EA'; MUT='#8FA89A'; G='#16C784'; Y='#FFC107'; R='#FF8A8A'; B='#40C4FF'; O='#EF9F27'
def style(ax,fig):
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=MUT,length=0); ax.grid(axis='y',color=GRID,lw=.8); ax.set_axisbelow(True)
def idr(x,d=1): return f"{x:,.{d}f}".replace(',','X').replace('.',',').replace('X','.')
# Chart 1: breakeven
tx=np.linspace(0,180,400)  # juta/hari
net=(20e6 - tx*1e6*365*0.00058)/1210e6*100
fig,ax=plt.subplots(figsize=(8,4.2),dpi=170); style(ax,fig)
ax.axhline(0,color=MUT,lw=1)
ax.fill_between(tx,net,0,where=net>=0,color=O,alpha=.12); ax.fill_between(tx,net,0,where=net<0,color=G,alpha=.15)
ax.plot(tx,net,color=TXT,lw=2)
ax.axvspan(30,50,color=Y,alpha=.10); ax.axvspan(70,170,color=B,alpha=.07)
for x,lab,c in [(9.5,'Kini\n±9,5 jt',G),(94.5,'Impas\n±91–95 jt',Y)]:
    ax.axvline(x,color=c,lw=1.2,ls='--'); ax.text(x+2,1.35,lab,color=c,fontsize=8.5,va='top',fontweight='bold')
ax.text(40,-1.1,'Seukuran\nLighter',color=Y,ha='center',fontsize=8); ax.text(120,-1.1,'Seukuran Hyperliquid',color=B,ha='center',fontsize=8)
ax.text(140,0.25,'APT menyusut (deflasi)',color=G,fontsize=9,ha='center',fontweight='bold'); ax.text(28,0.95,'Suplai masih naik',color=O,fontsize=9,fontweight='bold')
ax.set_xlim(0,180); ax.set_ylim(-1.6,1.8)
ax.set_xlabel('Transaksi per hari (juta)',color=MUT); ax.set_ylabel('Suplai bersih per tahun (%)',color=MUT)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,p: idr(v,1).replace('-','−')+'%'))
ax.set_title('Berapa transaksi agar APT berhenti bertambah?',color=TXT,loc='left',fontsize=12.5,fontweight='bold',pad=12)
fig.text(0.01,0.01,'Asumsi Messari: APT baru ±20 juta/th, dibakar ±0,00058 APT per transaksi, suplai 1,21 miliar. Hitungan Shariacrypto (est.).',color=MUT,fontsize=7.2)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('impas.png',facecolor=BG); plt.close(fig)
# Chart 2: APT vs BTC indexed
apt=[3.5824,3.38,3.2379,2.8288,2.337,1.9884,1.707,1.6174,1.5763,1.7219,1.939,1.7672,1.7301,1.4866,1.2369,1.0679,0.933,0.8409,0.9289,0.9286,0.9341,0.928,0.9202,0.8492,0.8114,0.9113,0.9844,0.987,1.1536,0.9282,0.9446,0.9436,0.6702,0.6799,0.6471,0.5744,0.6319,0.6101,0.5946,0.6275,0.562,0.5887,0.5179,0.6396,0.5181,0.6244,0.5881,0.7379,0.8654,0.8017,0.9005,0.7838,0.8277]
btc=[114472.45,110639.63,104719.64,94177.08,86805.01,90394.31,90405.64,88175.18,88621.75,87835.84,91413.49,90827.46,93634.43,86572.22,76974.45,70264.73,68788.19,67659.39,65738.1,65969.78,72789.91,67845.21,65954.92,68981.9,70753.41,73856.35,78657.54,78538.23,82138.93,77429.35,76981.13,73579.69,63239.52,65710.4,63237.54,59532.34,63547.88,63758.22,64690.8,65340.3,63482.0,64844.89,62818.65,77755.27,77667.57,80350.05,76838.16,81142.61,84458.09,86480.3,83679.47,82017.6,82941.0]
d0=dt.date(2025,10,20); dates=[d0+dt.timedelta(weeks=i) for i in range(len(apt))]
ia=np.array(apt)/apt[0]*100; ib=np.array(btc)/btc[0]*100
fig,ax=plt.subplots(figsize=(8,4.2),dpi=170); style(ax,fig)
ax.plot(dates,ib,color=Y,lw=2,label='BTC'); ax.plot(dates,ia,color=G,lw=2.2,label='APT')
ax.text(dates[-1]+dt.timedelta(days=4),ib[-1],'BTC '+idr(ib[-1]-100,0).replace('-','−')+'%',color=Y,fontsize=8.5,va='center',fontweight='bold')
ax.text(dates[-1]+dt.timedelta(days=4),ia[-1],'APT '+idr(ia[-1]-100,0).replace('-','−')+'%',color=G,fontsize=8.5,va='center',fontweight='bold')
ax.axvspan(dt.date(2026,3,1),dt.date(2026,3,19),color=MUT,alpha=.12)
ax.text(dt.date(2026,3,10),103,'1–19 Mar: batas suplai,\nstaking ½, gas 10×',color=MUT,fontsize=7.3,ha='center',va='bottom')
ax.axvline(dt.date(2026,10,12),color=MUT,lw=.9,ls=':'); ax.text(dt.date(2026,10,12),103,'12 Okt: unlock\ntim & investor selesai',color=MUT,fontsize=7.3,ha='right',va='bottom')
ax.set_ylim(0,118); ax.set_xlim(dates[0],dates[-1]+dt.timedelta(days=40))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,p: idr(v,0)))
import matplotlib.dates as md; ax.xaxis.set_major_formatter(md.DateFormatter('%b %y'))
ax.set_title('APT vs BTC, 52 minggu (20 Okt 2025 = 100)',color=TXT,loc='left',fontsize=12.5,fontweight='bold',pad=12)
fig.text(0.01,0.01,'Sumber: Yahoo Finance, penutupan mingguan s.d. 19 Okt 2026. Beta 1,32 (hitungan Shariacrypto).',color=MUT,fontsize=7.2)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('apt_btc.png',facecolor=BG); plt.close(fig)
