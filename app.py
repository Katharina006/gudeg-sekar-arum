import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Gudeg Sekar Arum | Dashboard Penjualan", layout="wide")

# Warna dashboard
BG = "#F4F2EA"
WHITE = "#FFFFFF"
DARK = "#203B2C"
SAGE = "#C8E6C9"
SAGE_BORDER = "#8BBF91"
GREEN = "#238636"
RED = "#D94841"
YELLOW = "#F2C94C"
BLUE = "#547D8A"
TEXT = "#26352C"
MUTED = "#526358"
GRID = "#E1E5DC"

# CSS: warna tetap terbaca pada tema terang/gelap
st.markdown(f"""
<style>
.stApp, [data-testid="stMain"] {{ background:{BG} !important; color:{TEXT} !important; }}
[data-testid="stHeader"] {{ background:{BG} !important; }}
.block-container {{ max-width:1600px; padding-top:1.4rem; }}
[data-testid="stSidebar"] {{ background:{DARK} !important; }}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {{ color:#F7F7F0 !important; }}
[data-testid="stSidebar"] [data-baseweb="select"] > div {{ background:#FFFFFF !important; border-color:{SAGE} !important; }}
[data-testid="stSidebar"] [data-baseweb="select"] input {{ color:{TEXT} !important; -webkit-text-fill-color:{TEXT} !important; }}
/* Paksa chip pilihan multiselect menjadi hijau muda, bukan merah */
[data-testid="stSidebar"] [data-baseweb="tag"],
[data-testid="stSidebar"] [data-baseweb="tag"] > span,
[data-testid="stSidebar"] [data-baseweb="tag"] > div,
[data-testid="stSidebar"] [data-baseweb="tag"] button,
[data-testid="stSidebar"] [data-baseweb="tag"] [role="button"] {
    background-color: {SAGE} !important;
    background: {SAGE} !important;
    border-color: {SAGE_BORDER} !important;
    color: {DARK} !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] [data-baseweb="tag"]:hover,
[data-testid="stSidebar"] [data-baseweb="tag"] button:hover {
    background-color: #B7DDBB !important;
    background: #B7DDBB !important;
}
[data-testid="stSidebar"] [data-baseweb="tag"] *,
[data-testid="stSidebar"] [data-baseweb="tag"] svg,
[data-testid="stSidebar"] [data-baseweb="tag"] path {
    color: {DARK} !important;
    fill: {DARK} !important;
    stroke: {DARK} !important;
}
[data-testid="stSidebar"] [data-testid="stDateInput"] label,
[data-testid="stSidebar"] [data-testid="stDateInput"] input,
[data-testid="stSidebar"] [data-testid="stDateInput"] input::placeholder,
[data-testid="stSidebar"] [data-testid="stDateInput"] button,
[data-testid="stSidebar"] [data-testid="stDateInput"] button * {{ color:{DARK} !important; -webkit-text-fill-color:{DARK} !important; opacity:1 !important; }}
[data-testid="stSidebar"] [data-testid="stDateInput"] [data-baseweb="input"] > div {{ background:#FFFFFF !important; border-color:{SAGE} !important; }}
[data-testid="stSidebar"] [data-testid="stDateInput"] svg {{ color:{DARK} !important; fill:{DARK} !important; }}
[data-testid="stDateInput"] input {{ background:#FFFFFF !important; color:{DARK} !important; -webkit-text-fill-color:{DARK} !important; }}
[data-testid="stDataFrame"] {{ background:#FFFFFF !important; }}
[data-testid="stDownloadButton"] button {{ background:{DARK} !important; color:#FFFFFF !important; border:1px solid {DARK} !important; }}
[data-testid="stDownloadButton"] button * {{ color:#FFFFFF !important; }}
[data-testid="stRadio"] label, [data-testid="stRadio"] p {{ color:{TEXT} !important; }}
[data-testid="stCaptionContainer"] p {{ color:{MUTED} !important; }}
.hero {{ background:linear-gradient(115deg,#E5EADD,#FFFDF5,#E7EBDD); border:1px solid #D9E0D3; border-radius:22px; padding:30px 34px; margin-bottom:24px; }}
.hero h1 {{ color:{DARK} !important; font-family:Georgia,serif; font-size:clamp(30px,3.5vw,46px); margin:0; }}
.hero .loc {{ color:{GREEN} !important; font-weight:700; letter-spacing:5px; margin-top:8px; }}
.hero .desc {{ color:{MUTED} !important; margin-bottom:0; }}
.section-title {{ color:{DARK} !important; font-family:Georgia,serif; font-size:25px; font-weight:700; margin-top:22px; }}
.section-subtitle {{ color:{MUTED} !important; font-size:13px; margin-bottom:12px; }}
.kpi {{ background:#FFFFFF; border:1px solid #E0E4DA; border-radius:15px; padding:17px; min-height:125px; }}
.kpi-label {{ color:{MUTED} !important; font-size:11px; font-weight:700; text-transform:uppercase; }}
.kpi-value {{ color:{DARK} !important; font-size:clamp(18px,1.6vw,25px); font-weight:700; margin-top:10px; overflow-wrap:anywhere; }}
.kpi-note {{ color:{MUTED} !important; font-size:11px; margin-top:7px; }}
.insight {{ background:#E8EEE4; border-left:4px solid {GREEN}; border-radius:10px; padding:13px 15px; margin:10px 0; color:{TEXT} !important; line-height:1.6; font-size:13px; }}
.insight b {{ color:{DARK} !important; }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Gudeg Sekar Arum</h1>
<div class="loc">Y O G Y A K A R T A</div>
<p class="desc">Dashboard analisis penjualan untuk memahami omzet, transaksi, performa outlet, kanal penjualan, dan pola penjualan berdasarkan jenis hari.</p>
</div>
""", unsafe_allow_html=True)

# File Excel harus berada di folder yang sama dengan app.py
EXCEL_NAME = "Data_Simulasi_Penjualan_Gudeg_Jogja_2025.xlsx"
EXCEL_PATH = Path(__file__).resolve().parent / EXCEL_NAME

@st.cache_data(show_spinner="Memuat data Excel...")
def load_data(path):
    try:
        frame = pd.read_excel(path, sheet_name="Data_Penjualan")
    except ValueError:
        frame = pd.read_excel(path, sheet_name=0)
    frame.columns = frame.columns.astype(str).str.strip()
    required = ["Tanggal", "Jenis_Hari", "Outlet", "Kanal_Penjualan", "Jumlah_Transaksi", "Omzet_Bersih_Rp", "Rating_Rata_rata", "Jumlah_Ulasan"]
    missing = [c for c in required if c not in frame.columns]
    if missing:
        raise ValueError("Kolom Excel tidak ditemukan: " + ", ".join(missing))
    frame["Tanggal"] = pd.to_datetime(frame["Tanggal"], errors="coerce", dayfirst=True)
    for c in ["Jumlah_Transaksi", "Omzet_Bersih_Rp", "Rating_Rata_rata", "Jumlah_Ulasan"]:
        frame[c] = pd.to_numeric(frame[c], errors="coerce")
    for c in ["Jenis_Hari", "Outlet", "Kanal_Penjualan"]:
        frame[c] = frame[c].astype("string").str.strip()
    frame = frame.dropna(subset=["Tanggal"]).copy()
    for c in ["Jumlah_Transaksi", "Omzet_Bersih_Rp", "Jumlah_Ulasan"]:
        frame[c] = frame[c].fillna(0)
    return frame

try:
    if not EXCEL_PATH.exists():
        st.error(f"File Excel tidak ditemukan: {EXCEL_NAME}. Unggah file tersebut ke repository yang sama dengan app.py.")
        st.stop()
    df = load_data(str(EXCEL_PATH))
except Exception as exc:
    st.error(f"Gagal membaca Excel: {exc}")
    st.stop()

if df.empty:
    st.error("File Excel tidak berisi data dengan tanggal yang valid.")
    st.stop()

# Sidebar filter
st.sidebar.markdown("""
<div style="background:#314C39;border:1px solid #8FA58A;border-radius:12px;padding:13px 15px;margin-bottom:14px">
<div style="color:#FFFFFF;font-size:23px;font-weight:700">Pusat Filter</div>
<div style="color:#E2EBDD;font-size:13px;margin-top:5px">Pilih data yang ingin dianalisis.</div>
</div>
""", unsafe_allow_html=True)

outlet_opts = sorted(df["Outlet"].dropna().astype(str).unique().tolist())
channel_opts = sorted(df["Kanal_Penjualan"].dropna().astype(str).unique().tolist())
day_opts = sorted(df["Jenis_Hari"].dropna().astype(str).unique().tolist())
sel_outlets = st.sidebar.multiselect("Outlet", outlet_opts, default=outlet_opts)
sel_channels = st.sidebar.multiselect("Kanal Penjualan", channel_opts, default=channel_opts)
sel_days = st.sidebar.multiselect("Jenis Hari", day_opts, default=day_opts)
min_date, max_date = df["Tanggal"].min().date(), df["Tanggal"].max().date()
dates = st.sidebar.date_input("Rentang Tanggal", value=(min_date, max_date), min_value=min_date, max_value=max_date, format="DD/MM/YYYY")
if isinstance(dates, (tuple, list)):
    if len(dates) == 2:
        start_date, end_date = dates
    elif len(dates) == 1:
        start_date = end_date = dates[0]
    else:
        st.warning("Pilih rentang tanggal.")
        st.stop()
else:
    start_date = end_date = dates
if start_date > end_date:
    st.sidebar.error("Tanggal awal tidak boleh setelah tanggal akhir.")
    st.stop()

data = df[
    df["Outlet"].astype(str).isin(sel_outlets)
    & df["Kanal_Penjualan"].astype(str).isin(sel_channels)
    & df["Jenis_Hari"].astype(str).isin(sel_days)
    & (df["Tanggal"].dt.date >= start_date)
    & (df["Tanggal"].dt.date <= end_date)
].copy()
if data.empty:
    st.warning("Tidak ada data yang sesuai dengan filter. Pilih kategori atau rentang tanggal lain.")
    st.stop()

def rupiah(value):
    return "Rp " + f"{value:,.0f}".replace(",", ".")

chart_font = dict(family="Arial, sans-serif", size=12, color=TEXT)
chart_config = {"displayModeBar": True, "responsive": True}

# KPI
revenue = data["Omzet_Bersih_Rp"].sum()
transactions = data["Jumlah_Transaksi"].sum()
avg_transaction = revenue / transactions if transactions else 0
ratings = data[data["Rating_Rata_rata"].notna() & (data["Jumlah_Ulasan"] > 0)]
review_total = ratings["Jumlah_Ulasan"].sum()
weighted_rating = (ratings["Rating_Rata_rata"].mul(ratings["Jumlah_Ulasan"]).sum() / review_total) if review_total else 0
st.markdown('<div class="section-title">Ringkasan Performa</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-subtitle">Periode {start_date:%d/%m/%Y} – {end_date:%d/%m/%Y}. Nilai mengikuti filter aktif.</div>', unsafe_allow_html=True)
kpi_cols = st.columns(4)
for col, (label, value, note) in zip(kpi_cols, [
    ("Omzet Bersih", rupiah(revenue), "Total omzet pada filter"),
    ("Jumlah Transaksi", f"{transactions:,.0f}".replace(",", "."), "Total transaksi terpilih"),
    ("Rata-rata Transaksi", rupiah(avg_transaction), "Omzet dibagi transaksi"),
    ("Rating Berbobot", f"{weighted_rating:.2f} / 5", "Dibobot jumlah ulasan")
]):
    with col:
        st.markdown(f'<div class="kpi"><div class="kpi-label">{label}</div><div class="kpi-value">{value}</div><div class="kpi-note">{note}</div></div>', unsafe_allow_html=True)

# Tren omzet
st.markdown('<div class="section-title">Tren Omzet Bersih</div><div class="section-subtitle">Lihat perubahan omzet dari waktu ke waktu.</div>', unsafe_allow_html=True)
period_mode = st.radio("Kelompokkan tren", ["Bulanan", "Mingguan"], horizontal=True)
trend = data.copy()
if period_mode == "Bulanan":
    trend["Periode"] = trend["Tanggal"].dt.to_period("M").dt.to_timestamp()
    trend["Label"] = trend["Periode"].dt.strftime("%b %Y")
else:
    trend["Periode"] = trend["Tanggal"].dt.to_period("W-SUN").dt.start_time
    trend["Label"] = trend["Periode"].dt.strftime("%d %b")
trend = trend.groupby(["Periode", "Label"], as_index=False)["Omzet_Bersih_Rp"].sum().sort_values("Periode")
trend_max = trend["Omzet_Bersih_Rp"].max()
trend_min = trend["Omzet_Bersih_Rp"].min()
trend_colors = [GREEN if v == trend_max else RED if v == trend_min else BLUE for v in trend["Omzet_Bersih_Rp"]]
fig_trend = px.area(trend, x="Label", y="Omzet_Bersih_Rp", markers=True, labels={"Label":"Periode", "Omzet_Bersih_Rp":"Omzet (Rp)"})
fig_trend.update_traces(line=dict(color=BLUE, width=3), fillcolor="rgba(84,125,138,0.18)", marker=dict(color=trend_colors, size=10, line=dict(color=WHITE, width=1.5)), hovertemplate="<b>%{x}</b><br>Omzet: Rp %{y:,.0f}<extra></extra>")
if len(trend):
    maxrow = trend.loc[trend["Omzet_Bersih_Rp"].idxmax()]
    minrow = trend.loc[trend["Omzet_Bersih_Rp"].idxmin()]
    fig_trend.add_annotation(x=maxrow["Label"], y=maxrow["Omzet_Bersih_Rp"], text="TERTINGGI", showarrow=True, ax=0, ay=-30, bgcolor="#E4F5E8", font=dict(color=GREEN))
    if maxrow["Label"] != minrow["Label"]:
        fig_trend.add_annotation(x=minrow["Label"], y=minrow["Omzet_Bersih_Rp"], text="TERENDAH", showarrow=True, ax=0, ay=30, bgcolor="#FDE8E7", font=dict(color=RED))
fig_trend.update_layout(height=390, paper_bgcolor=WHITE, plot_bgcolor=WHITE, font=chart_font, margin=dict(l=15,r=15,t=35,b=20), hoverlabel=dict(bgcolor=WHITE,font=dict(color=TEXT)))
fig_trend.update_xaxes(color=TEXT, showgrid=False, automargin=True)
fig_trend.update_yaxes(color=TEXT, gridcolor=GRID, tickformat="~s")
st.plotly_chart(fig_trend, use_container_width=True, config=chart_config)

# Bar charts outlet dan channel
st.markdown('<div class="section-title">Perbandingan Kinerja</div><div class="section-subtitle">Merah menandai nilai terendah, hijau tertinggi. Nilai ditampilkan langsung pada batang.</div>', unsafe_allow_html=True)
outlet_sales = data.groupby("Outlet", as_index=False)["Omzet_Bersih_Rp"].sum().sort_values("Omzet_Bersih_Rp")
channel_sales = data.groupby("Kanal_Penjualan", as_index=False)["Omzet_Bersih_Rp"].sum().sort_values("Omzet_Bersih_Rp")
palette = [RED, YELLOW, BLUE, GREEN]
def ranked_colors(n):
    if n <= 1:
        return [GREEN] * n
    return [palette[round(i * (len(palette)-1) / (n-1))] for i in range(n)]
left, right = st.columns(2)
for col, frame, category, title in [
    (left, outlet_sales, "Outlet", "Omzet per Outlet"),
    (right, channel_sales, "Kanal_Penjualan", "Omzet per Kanal Penjualan")
]:
    with col:
        fig = px.bar(frame, x="Omzet_Bersih_Rp", y=category, orientation="h", text="Omzet_Bersih_Rp", title=title, labels={category:category.replace("_", " "), "Omzet_Bersih_Rp":"Omzet (Rp)"})
        fig.update_traces(marker_color=ranked_colors(len(frame)), marker_line_color=WHITE, marker_line_width=1.2, texttemplate="Rp %{x:,.0f}", textposition="outside", cliponaxis=False, hovertemplate="<b>%{y}</b><br>Omzet: Rp %{x:,.0f}<extra></extra>")
        fig.update_layout(height=380, margin=dict(l=20,r=85,t=55,b=30), paper_bgcolor=WHITE, plot_bgcolor=WHITE, showlegend=False, font=chart_font, title_font=dict(color=TEXT), hoverlabel=dict(bgcolor=WHITE,font=dict(color=TEXT)))
        fig.update_xaxes(color=TEXT, gridcolor=GRID, tickformat="~s")
        fig.update_yaxes(color=TEXT, showgrid=False, automargin=True)
        st.plotly_chart(fig, use_container_width=True, config=chart_config)

# Pie chart
st.markdown('<div class="section-title">Pola Penjualan</div><div class="section-subtitle">Kontribusi setiap jenis hari terhadap total omzet.</div>', unsafe_allow_html=True)
day_sales = data.groupby("Jenis_Hari", as_index=False)["Omzet_Bersih_Rp"].sum().sort_values("Omzet_Bersih_Rp", ascending=False)
pie_palette = [GREEN, BLUE, YELLOW, RED]
pie_colors = [pie_palette[round(i*(len(pie_palette)-1)/max(len(day_sales)-1,1))] for i in range(len(day_sales))]
pie_col, insight_col = st.columns([1,1])
with pie_col:
    figpie = px.pie(day_sales, names="Jenis_Hari", values="Omzet_Bersih_Rp", hole=0.48, title="Kontribusi Omzet per Jenis Hari", color_discrete_sequence=pie_colors)
    figpie.update_traces(textposition="inside", textinfo="label+percent", marker=dict(line=dict(color=WHITE,width=2)), hovertemplate="<b>%{label}</b><br>Omzet: Rp %{value:,.0f}<br>Kontribusi: %{percent}<extra></extra>")
    figpie.update_layout(height=380, paper_bgcolor=WHITE, font=chart_font, title_font=dict(color=TEXT), legend=dict(font=dict(color=TEXT)), hoverlabel=dict(bgcolor=WHITE,font=dict(color=TEXT)))
    st.plotly_chart(figpie, use_container_width=True, config=chart_config)
with insight_col:
    st.markdown('<div class="section-title" style="font-size:23px">Insight Otomatis</div>', unsafe_allow_html=True)
    best_outlet = outlet_sales.iloc[-1]
    worst_outlet = outlet_sales.iloc[0]
    best_channel = channel_sales.iloc[-1]
    best_day = day_sales.iloc[0]
    st.markdown(f'<div class="insight"><b>Outlet omzet tertinggi</b><br>{best_outlet["Outlet"]}: {rupiah(best_outlet["Omzet_Bersih_Rp"])} ({best_outlet["Omzet_Bersih_Rp"] / revenue * 100 if revenue else 0:.1f}% dari omzet terfilter).</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="insight"><b>Outlet omzet terendah</b><br>{worst_outlet["Outlet"]}: {rupiah(worst_outlet["Omzet_Bersih_Rp"])}.</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="insight"><b>Kanal penjualan terkuat</b><br>{best_channel["Kanal_Penjualan"]}: {rupiah(best_channel["Omzet_Bersih_Rp"])}.</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="insight"><b>Jenis hari omzet tertinggi</b><br>{best_day["Jenis_Hari"]}: {rupiah(best_day["Omzet_Bersih_Rp"])} ({best_day["Omzet_Bersih_Rp"] / revenue * 100 if revenue else 0:.1f}% dari omzet terfilter).</div>', unsafe_allow_html=True)

# Tabel detail selalu terlihat, bukan disembunyikan dalam expander
st.markdown('<div class="section-title">Lihat Detail Data Penjualan</div><div class="section-subtitle">Tabel di bawah mengikuti filter yang aktif. Unduh hasilnya sebagai CSV.</div>', unsafe_allow_html=True)
detail = data.sort_values("Tanggal", ascending=False)
st.dataframe(detail, use_container_width=True, hide_index=True, height=420)
st.download_button("Download Data Penjualan (CSV)", data=detail.to_csv(index=False).encode("utf-8-sig"), file_name="data_penjualan_gudeg.csv", mime="text/csv")
st.markdown("---")
st.markdown(f'<div style="text-align:center;color:{MUTED};font-size:11px;padding:15px">GUDEG SEKAR ARUM · YOGYAKARTA<br>{len(data):,} baris setelah filter · {data["Tanggal"].min():%d/%m/%Y} – {data["Tanggal"].max():%d/%m/%Y}<br>Data simulasi untuk pembelajaran.</div>', unsafe_allow_html=True)
