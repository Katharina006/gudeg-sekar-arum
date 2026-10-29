
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Gudeg Sekar Arum Yogyakarta",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Palet warna
BG = "#F4F2EA"
WHITE = "#FFFFFF"
DARK = "#203B2C"
GREEN = "#238636"
SAGE = "#A9BBA3"
SAGE_DARK = "#314C39"
BLUE = "#547D8A"
YELLOW = "#F2C94C"
RED = "#D66A62"
TEXT = "#26352C"
MUTED = "#526358"
GRID = "#E1E5DC"

# CSS agar warna teks tidak mengikuti mode gelap/terang
st.markdown(f"""
<style>
.stApp, [data-testid="stMain"] {{
    background: {BG} !important;
    color: {TEXT} !important;
}}
[data-testid="stHeader"] {{ background: {BG} !important; }}
.block-container {{ max-width: 1600px; padding-top: 1.4rem; }}

[data-testid="stSidebar"] {{ background: {DARK} !important; }}
[data-testid="stSidebar"] * {{ color: #F7F7F0; }}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
    color: #E2EBDD !important;
    opacity: 1 !important;
}}
[data-testid="stSidebar"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-baseweb="input"] > div {{
    background: {SAGE_DARK} !important;
    border-color: #8FA58A !important;
}}
[data-testid="stSidebar"] input {{
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}}

/* Pilihan filter memakai warna sage, bukan merah */
[data-testid="stSidebar"] [data-baseweb="tag"] {{
    background: {SAGE} !important;
    border: 1px solid #D7E1D2 !important;
    border-radius: 7px !important;
}}
[data-testid="stSidebar"] [data-baseweb="tag"] *,
[data-testid="stSidebar"] [data-baseweb="tag"] svg {{
    color: {DARK} !important;
    fill: {DARK} !important;
}}
[data-baseweb="popover"] li {{ color: {TEXT} !important; }}

/* Rentang tanggal */
[data-testid="stDateInput"] label {{ color: {TEXT} !important; }}
[data-testid="stDateInput"] input {{
    background: #FFFFFF !important;
    color: {TEXT} !important;
    -webkit-text-fill-color: {TEXT} !important;
    border-color: #B8C7B5 !important;
}}
[data-testid="stDateInput"] button {{
    background: #FFFFFF !important;
    color: {TEXT} !important;
}}

/* Header dashboard */
.hero {{
    background: linear-gradient(115deg,#E5EADD,#FFFDF5,#E7EBDD);
    border: 1px solid #D9E0D3;
    border-radius: 22px;
    padding: 30px 34px;
    margin-bottom: 24px;
}}
.hero-title {{
    color: {DARK} !important;
    font-family: Georgia,serif;
    font-size: clamp(30px,3.5vw,46px);
    font-weight: 700;
    margin: 0;
}}
.hero-location {{
    color: {GREEN} !important;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 5px;
    margin-top: 8px;
}}
.hero-description {{
    color: {MUTED} !important;
    font-size: 14px;
    margin-top: 12px;
}}
.section-title {{
    color: {DARK} !important;
    font-family: Georgia,serif;
    font-size: 25px;
    font-weight: 700;
    margin-top: 22px;
    margin-bottom: 4px;
}}
.section-subtitle {{
    color: {MUTED} !important;
    font-size: 13px;
    margin-bottom: 14px;
}}

/* Kartu ringkasan */
.kpi-card {{
    background: #FFFFFF;
    border: 1px solid #E0E4DA;
    border-radius: 15px;
    padding: 18px;
    min-height: 128px;
}}
.kpi-label {{
    color: {MUTED} !important;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
}}
.kpi-value {{
    color: {DARK} !important;
    font-size: clamp(18px,1.6vw,25px);
    font-weight: 700;
    margin-top: 12px;
    overflow-wrap: anywhere;
}}
.kpi-note {{
    color: #657568 !important;
    font-size: 11px;
    margin-top: 7px;
}}
.insight-card {{
    background: #E8EEE4;
    border-left: 4px solid {GREEN};
    border-radius: 10px;
    padding: 14px 16px;
    margin: 11px 0;
    color: {TEXT} !important;
    font-size: 13px;
    line-height: 1.65;
}}
.insight-card b {{ color: {DARK} !important; }}

/* Detail tabel dan download */
[data-testid="stDataFrame"] {{ background: #FFFFFF !important; }}
[data-testid="stDataFrame"] * {{ color: {TEXT} !important; }}
[data-testid="stDownloadButton"] button {{
    background: {DARK} !important;
    color: #FFFFFF !important;
    border: 1px solid {DARK} !important;
}}
[data-testid="stDownloadButton"] button * {{
    color: #FFFFFF !important;
}}
[data-testid="stRadio"] label,
[data-testid="stRadio"] p {{ color: {TEXT} !important; }}
[data-testid="stCaptionContainer"] p {{ color: {MUTED} !important; }}
.footer {{
    text-align: center;
    color: #657568 !important;
    font-size: 11px;
    padding: 18px 8px;
}}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
  <p class="hero-title">Gudeg Sekar Arum</p>
  <div class="hero-location">Y O G Y A K A R T A</div>
  <p class="hero-description">
    Dashboard analisis penjualan untuk memantau omzet,
    membandingkan performa outlet dan kanal penjualan,
    serta memahami pola penjualan berdasarkan jenis hari.
  </p>
</div>
""", unsafe_allow_html=True)

# Baca Excel dari folder yang sama dengan app.py
EXCEL_FILE = "Data_Simulasi_Penjualan_Gudeg_Jogja_2025.xlsx"

try:
    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="Data_Penjualan")
    except ValueError:
        df = pd.read_excel(EXCEL_FILE, sheet_name=0)

    df.columns = df.columns.astype(str).str.strip()

    required = [
        "Tanggal", "Jenis_Hari", "Outlet", "Kanal_Penjualan",
        "Jumlah_Transaksi", "Omzet_Bersih_Rp",
        "Rating_Rata_rata", "Jumlah_Ulasan"
    ]
    missing = [c for c in required if c not in df.columns]

    if missing:
        st.error("Kolom Excel tidak ditemukan: " + ", ".join(missing))
        st.stop()

    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"], errors="coerce", dayfirst=True
    )

    for col in [
        "Jumlah_Transaksi", "Omzet_Bersih_Rp",
        "Rating_Rata_rata", "Jumlah_Ulasan"
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["Outlet", "Kanal_Penjualan", "Jenis_Hari"]:
        df[col] = df[col].astype("string").str.strip()

    df = df.dropna(subset=["Tanggal"]).copy()

    for col in ["Jumlah_Transaksi", "Omzet_Bersih_Rp", "Jumlah_Ulasan"]:
        df[col] = df[col].fillna(0)

    if df.empty:
        st.error("Tidak ada data penjualan dengan tanggal valid.")
        st.stop()

    # SIDEBAR: tulisan petunjuk selalu ditampilkan
    st.sidebar.markdown(
        "<h2 style='color:#F7F7F0 !important;margin-bottom:4px'>"
        "Pusat Filter</h2>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        "<p style='color:#E2EBDD !important;font-size:14px;"
        "margin-top:0;margin-bottom:16px'>"
        "Pilih data yang ingin dianalisis.</p>",
        unsafe_allow_html=True
    )

    outlet_options = sorted(df["Outlet"].dropna().unique().tolist())
    channel_options = sorted(
        df["Kanal_Penjualan"].dropna().unique().tolist()
    )
    day_options = sorted(df["Jenis_Hari"].dropna().unique().tolist())

    selected_outlets = st.sidebar.multiselect(
        "Outlet", outlet_options, default=outlet_options
    )
    selected_channels = st.sidebar.multiselect(
        "Kanal Penjualan", channel_options, default=channel_options
    )
    selected_days = st.sidebar.multiselect(
        "Jenis Hari", day_options, default=day_options
    )

    min_date = df["Tanggal"].min().date()
    max_date = df["Tanggal"].max().date()

    date_range = st.sidebar.date_input(
        "Rentang Tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY"
    )

    if isinstance(date_range, (tuple, list)):
        if len(date_range) == 2:
            start_date, end_date = date_range
        elif len(date_range) == 1:
            start_date = end_date = date_range[0]
        else:
            st.sidebar.warning("Pilih rentang tanggal.")
            st.stop()
    else:
        start_date = end_date = date_range

    if start_date > end_date:
        st.sidebar.error("Tanggal awal tidak boleh melewati tanggal akhir.")
        st.stop()

    data = df[
        df["Outlet"].isin(selected_outlets)
        & df["Kanal_Penjualan"].isin(selected_channels)
        & df["Jenis_Hari"].isin(selected_days)
        & (df["Tanggal"].dt.date >= start_date)
        & (df["Tanggal"].dt.date <= end_date)
    ].copy()

    if data.empty:
        st.warning("Tidak ada data sesuai filter. Ubah pilihan filter.")
        st.stop()

    def rupiah(value):
        return "Rp " + f"{value:,.0f}".replace(",", ".")

    # Ringkasan KPI
    revenue = data["Omzet_Bersih_Rp"].sum()
    transactions = data["Jumlah_Transaksi"].sum()
    average_transaction = revenue / transactions if transactions > 0 else 0

    rating_data = data[
        data["Rating_Rata_rata"].notna()
        & (data["Jumlah_Ulasan"] > 0)
    ]
    total_reviews = rating_data["Jumlah_Ulasan"].sum()
    weighted_rating = (
        (rating_data["Rating_Rata_rata"] * rating_data["Jumlah_Ulasan"]).sum()
        / total_reviews
        if total_reviews > 0 else 0
    )

    st.markdown(
        '<div class="section-title">Ringkasan Performa</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="section-subtitle">Periode '
        f'{start_date:%d/%m/%Y} – {end_date:%d/%m/%Y}. '
        f'Angka mengikuti filter yang dipilih.</div>',
        unsafe_allow_html=True
    )

    kpis = st.columns(4)
    kpi_items = [
        ("Omzet Bersih", rupiah(revenue), "Total pendapatan setelah diskon"),
        ("Jumlah Transaksi", f"{transactions:,.0f}".replace(",", "."),
         "Total transaksi terpilih"),
        ("Rata-rata Nilai Transaksi", rupiah(average_transaction),
         "Omzet dibagi jumlah transaksi"),
        ("Rating Berbobot", f"{weighted_rating:.2f} / 5",
         "Dibobot berdasarkan jumlah ulasan")
    ]

    for col, (label, value, note) in zip(kpis, kpi_items):
        with col:
            st.markdown(
                f'<div class="kpi-card">'
                f'<div class="kpi-label">{label}</div>'
                f'<div class="kpi-value">{value}</div>'
                f'<div class="kpi-note">{note}</div></div>',
                unsafe_allow_html=True
            )

    chart_font = dict(family="Arial, sans-serif", size=12, color=TEXT)
    chart_config = {"displayModeBar": False, "responsive": True}

    # TREN OMZET
    st.markdown(
        '<div class="section-title">Tren Omzet Bersih</div>'
        '<div class="section-subtitle">'
        'Pantau perubahan omzet berdasarkan waktu.</div>',
        unsafe_allow_html=True
    )

    period_choice = st.radio(
        "Kelompokkan tren berdasarkan",
        ["Bulanan", "Mingguan"],
        horizontal=True
    )

    trend = data.copy()

    if period_choice == "Bulanan":
        trend["Periode"] = trend["Tanggal"].dt.to_period("M").dt.to_timestamp()
        trend["Label"] = trend["Periode"].dt.strftime("%b %Y")
    else:
        trend["Periode"] = (
            trend["Tanggal"].dt.to_period("W-SUN").dt.start_time
        )
        week_end = trend["Periode"] + pd.Timedelta(days=6)
        trend["Label"] = (
            trend["Periode"].dt.strftime("%d %b")
            + " – " + week_end.dt.strftime("%d %b %Y")
        )

    trend = (
        trend.groupby(["Periode", "Label"], as_index=False)["Omzet_Bersih_Rp"]
        .sum().sort_values("Periode")
    )

    fig_trend = px.area(
        trend, x="Label", y="Omzet_Bersih_Rp", markers=True,
        labels={"Label": "Periode", "Omzet_Bersih_Rp": "Omzet Bersih (Rp)"}
    )

    if not trend.empty:
        hi = trend["Omzet_Bersih_Rp"].idxmax()
        lo = trend["Omzet_Bersih_Rp"].idxmin()

        colors = [
            GREEN if i == hi else RED if i == lo
            else BLUE if n % 2 == 0 else YELLOW
            for n, i in enumerate(trend.index)
        ]
        sizes = [13 if i in (hi, lo) else 8 for i in trend.index]

        fig_trend.update_traces(
            line=dict(color=BLUE, width=3),
            fillcolor="rgba(84,125,138,0.18)",
            marker=dict(
                size=sizes, color=colors,
                line=dict(color=WHITE, width=1.5)
            ),
            hovertemplate="<b>%{x}</b><br>Omzet: Rp %{y:,.0f}<extra></extra>"
        )

        maxrow = trend.loc[hi]
        minrow = trend.loc[lo]

        fig_trend.add_annotation(
            x=maxrow["Label"], y=maxrow["Omzet_Bersih_Rp"],
            text="TERTINGGI", showarrow=True, arrowhead=2,
            ax=0, ay=-35, font=dict(color=GREEN, size=10),
            bgcolor="#E4F5E8", bordercolor=GREEN, borderwidth=1
        )

        if hi != lo:
            fig_trend.add_annotation(
                x=minrow["Label"], y=minrow["Omzet_Bersih_Rp"],
                text="TERENDAH", showarrow=True, arrowhead=2,
                ax=0, ay=35, font=dict(color="#9F302B", size=10),
                bgcolor="#FCE9E7", bordercolor=RED, borderwidth=1
            )

    fig_trend.update_layout(
        height=390, margin=dict(l=20, r=20, t=25, b=25),
        paper_bgcolor=WHITE, plot_bgcolor=WHITE,
        font=chart_font,
        hoverlabel=dict(bgcolor=WHITE, font=dict(color=TEXT))
    )
    fig_trend.update_xaxes(
        color=TEXT, tickfont=dict(color=MUTED),
        showgrid=False, automargin=True
    )
    fig_trend.update_yaxes(
        color=TEXT, tickfont=dict(color=MUTED),
        gridcolor=GRID, tickformat="~s"
    )
    st.plotly_chart(fig_trend, use_container_width=True, config=chart_config)

    # PERBANDINGAN OUTLET DAN KANAL
    st.markdown(
        '<div class="section-title">Perbandingan Kinerja</div>'
        '<div class="section-subtitle">Merah = terendah, kuning dan biru = '
        'nilai menengah, hijau = tertinggi.</div>',
        unsafe_allow_html=True
    )

    outlet_sales = (
        data.groupby("Outlet", as_index=False)["Omzet_Bersih_Rp"]
        .sum().sort_values("Omzet_Bersih_Rp", ascending=True)
    )
    channel_sales = (
        data.groupby("Kanal_Penjualan", as_index=False)["Omzet_Bersih_Rp"]
        .sum().sort_values("Omzet_Bersih_Rp", ascending=True)
    )

    rank_palette = [RED, YELLOW, BLUE, GREEN]

    def rank_colors(n):
        if n <= 1:
            return [GREEN] * n
        return [
            rank_palette[round(i * (len(rank_palette) - 1) / (n - 1))]
            for i in range(n)
        ]

    c1, c2 = st.columns(2)

    for container, sales, category, title in [
        (c1, outlet_sales, "Outlet", "Kinerja per Outlet"),
        (c2, channel_sales, "Kanal_Penjualan", "Kinerja per Kanal Penjualan")
    ]:
        with container:
            fig = px.bar(
                sales, x="Omzet_Bersih_Rp", y=category,
                orientation="h", text="Omzet_Bersih_Rp",
                title=title,
                labels={
                    category: category.replace("_", " "),
                    "Omzet_Bersih_Rp": "Omzet Bersih (Rp)"
                }
            )

            positions = [
                "TERENDAH" if i == 0
                else "TERTINGGI" if i == len(sales) - 1
                else "MENENGAH"
                for i in range(len(sales))
            ]

            fig.update_traces(
                marker_color=rank_colors(len(sales)),
                marker_line_color=WHITE, marker_line_width=1.2,
                texttemplate="%{x:,.0f}", textposition="outside",
                cliponaxis=False, customdata=positions,
                hovertemplate="<b>%{y}</b><br>Omzet: Rp %{x:,.0f}"
                              "<br>Posisi: %{customdata}<extra></extra>"
            )
            fig.update_layout(
                height=380, margin=dict(l=20, r=90, t=60, b=35),
                paper_bgcolor=WHITE, plot_bgcolor=WHITE,
                showlegend=False, font=chart_font,
                title_font=dict(size=16, color=TEXT),
                hoverlabel=dict(bgcolor=WHITE, font=dict(color=TEXT))
            )
            fig.update_xaxes(
                color=TEXT, tickfont=dict(color=MUTED),
                gridcolor=GRID, tickformat="~s"
            )
            fig.update_yaxes(
                color=TEXT, tickfont=dict(color=TEXT),
                showgrid=False, automargin=True
            )
            st.plotly_chart(fig, use_container_width=True, config=chart_config)

    st.markdown(
        f'<div class="insight-card"><b>Keterangan warna:</b> '
        f'<span style="color:{RED};font-weight:700">Merah = terendah</span> · '
        f'<span style="color:#A77B00;font-weight:700">Kuning = rendah-menengah</span> · '
        f'<span style="color:{BLUE};font-weight:700">Biru = menengah-tinggi</span> · '
        f'<span style="color:{GREEN};font-weight:700">Hijau = tertinggi</span>. '
        f'Warna mengikuti nilai setelah filter diterapkan.</div>',
        unsafe_allow_html=True
    )

    # PIE CHART
    st.markdown(
        '<div class="section-title">Pola Penjualan</div>'
        '<div class="section-subtitle">Kontribusi omzet berdasarkan jenis hari.</div>',
        unsafe_allow_html=True
    )

    day_sales = (
        data.groupby("Jenis_Hari", as_index=False)["Omzet_Bersih_Rp"]
        .sum().sort_values("Omzet_Bersih_Rp", ascending=False)
    )

    pie_col, insight_col = st.columns([1, 1])

    with pie_col:
        pie_palette = [GREEN, BLUE, YELLOW, RED]
        pie_colors = [
            pie_palette[round(i * (len(pie_palette) - 1)
                               / max(len(day_sales) - 1, 1))]
            for i in range(len(day_sales))
        ]
        pulls = [
            0.08 if i in (0, len(day_sales) - 1) and len(day_sales) > 1 else 0
            for i in range(len(day_sales))
        ]

        fig_pie = px.pie(
            day_sales, names="Jenis_Hari", values="Omzet_Bersih_Rp",
            hole=0.5, title="Proporsi Omzet per Jenis Hari",
            color_discrete_sequence=pie_colors
        )
        fig_pie.update_traces(
            pull=pulls,
            marker=dict(line=dict(color=WHITE, width=2)),
            textposition="inside", textinfo="label+percent",
            insidetextfont=dict(color=TEXT, size=12),
            hovertemplate="<b>%{label}</b><br>Omzet: Rp %{value:,.0f}"
                          "<br>Kontribusi: %{percent}<extra></extra>"
        )
        fig_pie.update_layout(
            height=380, margin=dict(l=15, r=15, t=60, b=20),
            paper_bgcolor=WHITE, plot_bgcolor=WHITE,
            font=chart_font,
            title_font=dict(size=16, color=TEXT),
            legend=dict(font=dict(color=TEXT, size=12)),
            hoverlabel=dict(bgcolor=WHITE, font=dict(color=TEXT))
        )
        st.plotly_chart(fig_pie, use_container_width=True, config=chart_config)

    with insight_col:
        st.markdown(
            '<div class="section-title" style="font-size:23px">'
            'Insight Otomatis</div>',
            unsafe_allow_html=True
        )

        best_outlet = outlet_sales.iloc[-1]
        worst_outlet = outlet_sales.iloc[0]
        best_channel = channel_sales.iloc[-1]
        worst_channel = channel_sales.iloc[0]
        best_day = day_sales.iloc[0]

        st.markdown(
            f'<div class="insight-card"><b>Outlet tertinggi</b><br>'
            f'{best_outlet["Outlet"]}: '
            f'{rupiah(best_outlet["Omzet_Bersih_Rp"])} '
            f'({best_outlet["Omzet_Bersih_Rp"]/revenue*100 if revenue else 0:.1f}%).'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="insight-card"><b>Outlet terendah</b><br>'
            f'{worst_outlet["Outlet"]}: '
            f'{rupiah(worst_outlet["Omzet_Bersih_Rp"])}.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="insight-card"><b>Kanal tertinggi / terendah</b><br>'
            f'{best_channel["Kanal_Penjualan"]}: '
            f'{rupiah(best_channel["Omzet_Bersih_Rp"])} · '
            f'{worst_channel["Kanal_Penjualan"]}: '
            f'{rupiah(worst_channel["Omzet_Bersih_Rp"])}.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="insight-card"><b>Jenis hari omzet tertinggi</b><br>'
            f'{best_day["Jenis_Hari"]}: '
            f'{rupiah(best_day["Omzet_Bersih_Rp"])}.</div>',
            unsafe_allow_html=True
        )
        st.caption("Ringkasan diperbarui otomatis berdasarkan filter.")

    # DETAIL DATA: tidak memakai expander agar tidak tersembunyi
    st.markdown(
        '<div class="section-title">Lihat Detail Data Penjualan</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">Tabel ini menampilkan data '
        'sesuai filter yang dipilih di sidebar.</div>',
        unsafe_allow_html=True
    )

    detail = data.sort_values("Tanggal", ascending=False).copy()
    st.dataframe(
        detail, use_container_width=True, hide_index=True, height=400
    )

    st.download_button(
        "Download Data Penjualan (CSV)",
        data=detail.to_csv(index=False).encode("utf-8-sig"),
        file_name="data_penjualan_gudeg.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.markdown(
        f'<div class="footer">GUDEG SEKAR ARUM · YOGYAKARTA<br>'
        f'{len(data):,} baris data setelah filter<br>'
        f'{data["Tanggal"].min():%d/%m/%Y} – '
        f'{data["Tanggal"].max():%d/%m/%Y}<br>'
        f'Sumber: file Excel dalam repository aplikasi. '
        f'Data simulasi untuk pembelajaran.</div>',
        unsafe_allow_html=True
    )

except FileNotFoundError:
    st.error(
        f"File Excel '{EXCEL_FILE}' tidak ditemukan. "
        "Unggah file Excel ke repository GitHub yang sama dengan app.py."
    )
except Exception as error:
    st.error(f"Terjadi kesalahan saat membaca atau mengolah Excel: {error}")
