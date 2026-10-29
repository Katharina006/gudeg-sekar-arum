import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# KONFIGURASI
# =========================================================
st.set_page_config(
    page_title="Gudeg Sekar Arum Yogyakarta",
    layout="wide",
    initial_sidebar_state="expanded"
)

BG = "#F4F2EA"
CARD = "#FFFFFF"
DARK = "#203B2C"
GREEN = "#4F6B50"
SAGE = "#8FA58A"
ORANGE = "#C8753D"
BLUE = "#547D8A"
PURPLE = "#88718F"
RED = "#D94841"
YELLOW = "#F2C94C"
TEXT = "#26352C"
MUTED = "#526358"
GRID = "#E1E5DC"

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background-color: #F4F2EA !important;
    color: #26352C !important;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] {
    background: rgba(244,242,234,0.96) !important;
}
[data-testid="stMain"] {
    background-color: #F4F2EA !important;
}
.block-container {
    max-width: 1600px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #203B2C !important;
}
[data-testid="stSidebar"] * {
    color: #F7F7F0;
}
[data-testid="stSidebar"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-baseweb="input"] > div {
    background-color: #314C39 !important;
    border-color: #6C826C !important;
}
[data-testid="stSidebar"] input {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
[data-testid="stSidebar"] small {
    color: #DCE7D8 !important;
    opacity: 1 !important;
}

/* Warna pilihan filter, hijau sage bukan merah */
[data-testid="stSidebar"] [data-baseweb="tag"],
[data-testid="stSidebar"] [data-baseweb="tag"] > span,
[data-testid="stSidebar"] [data-baseweb="tag"] > div {
    background-color: #A9BBA3 !important;
    border: 1px solid #D7E1D2 !important;
    border-radius: 7px !important;
}
[data-testid="stSidebar"] [data-baseweb="tag"] *,
[data-testid="stSidebar"] [data-baseweb="tag"] svg,
[data-testid="stSidebar"] [data-baseweb="tag"] button {
    color: #203B2C !important;
    fill: #203B2C !important;
    background-color: transparent !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Teks umum */
.stMarkdown, .stMarkdown p, .stMarkdown label {
    color: #26352C;
}
h1, h2, h3, p, label {
    color: #26352C;
}

/* Tanggal tetap terbaca di mode terang maupun gelap */
[data-testid="stDateInput"] label,
[data-testid="stDateInput"] p,
[data-testid="stDateInput"] input,
[data-testid="stDateInput"] button,
[data-testid="stDateInput"] [data-baseweb="input"] > div,
[data-testid="stDateInput"] [data-baseweb="select"] > div {
    color: #203B2C !important;
    -webkit-text-fill-color: #203B2C !important;
    background-color: #FFFFFF !important;
    border-color: #B8C7B5 !important;
    opacity: 1 !important;
}
[data-testid="stDateInput"] svg {
    fill: #203B2C !important;
}
[data-testid="stSidebar"] [data-testid="stDateInput"] label *,
[data-testid="stSidebar"] [data-testid="stDateInput"] input,
[data-testid="stSidebar"] [data-testid="stDateInput"] input::placeholder,
[data-testid="stSidebar"] [data-testid="stDateInput"] button *,
[data-testid="stSidebar"] [data-testid="stDateInput"] [data-baseweb="input"] *,
[data-testid="stSidebar"] [data-testid="stDateInput"] [data-baseweb="select"] * {
    color: #203B2C !important;
    -webkit-text-fill-color: #203B2C !important;
    opacity: 1 !important;
}
[data-testid="stSidebar"] [data-testid="stDateInput"] [data-baseweb="input"] > div,
[data-testid="stSidebar"] [data-testid="stDateInput"] [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border-color: #A9BBA3 !important;
}
[data-testid="stSidebar"] [data-testid="stDateInput"] svg {
    fill: #203B2C !important;
    color: #203B2C !important;
}

/* Detail penjualan */
div[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid #C9D5C5 !important;
    border-radius: 12px !important;
}
div[data-testid="stExpander"] details,
div[data-testid="stExpander"] summary {
    background-color: #FFFFFF !important;
    color: #203B2C !important;
}
div[data-testid="stExpander"] summary p,
div[data-testid="stExpander"] summary span,
div[data-testid="stExpander"] summary svg,
div[data-testid="stExpander"] label {
    color: #203B2C !important;
    fill: #203B2C !important;
    opacity: 1 !important;
}
div[data-testid="stDataFrame"],
div[data-testid="stDataFrame"] *,
div[data-testid="stTable"] {
    background-color: #FFFFFF !important;
    color: #203B2C !important;
}

/* Tombol download */
div[data-testid="stDownloadButton"] button {
    background-color: #203B2C !important;
    color: #FFFFFF !important;
    border: 1px solid #203B2C !important;
    font-weight: 700 !important;
}
div[data-testid="stDownloadButton"] button p,
div[data-testid="stDownloadButton"] button span {
    color: #FFFFFF !important;
}

/* Header dashboard */
.hero {
    background: linear-gradient(115deg,#E5EADD 0%,#FFFDF5 55%,#E7EBDD 100%);
    border: 1px solid #D9E0D3;
    border-radius: 22px;
    padding: 32px 36px;
    margin-bottom: 25px;
    box-shadow: 0 5px 20px rgba(32,59,44,.06);
}
.hero-title {
    color: #203B2C !important;
    font-family: 'Playfair Display', serif;
    font-size: clamp(30px,3.5vw,46px);
    font-weight: 700;
    line-height: 1.2;
    margin: 0;
}
.hero-location {
    color: #4F6B50 !important;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 5px;
    margin-top: 8px;
}
.hero-description {
    color: #526358 !important;
    font-size: 14px;
    margin-top: 14px;
    margin-bottom: 0;
}

/* Judul bagian */
.section-title {
    color: #203B2C !important;
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    font-weight: 700;
    margin-top: 22px;
    margin-bottom: 4px;
}
.section-subtitle {
    color: #526358 !important;
    font-size: 13px;
    margin-bottom: 15px;
}

/* Kartu ringkasan */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E0E4DA;
    border-radius: 16px;
    padding: 19px;
    min-height: 135px;
    box-shadow: 0 4px 15px rgba(32,59,44,.045);
}
.kpi-label {
    color: #526358 !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .6px;
    text-transform: uppercase;
}
.kpi-value {
    color: #203B2C !important;
    font-size: clamp(18px,1.6vw,25px);
    font-weight: 700;
    margin-top: 12px;
    overflow-wrap: anywhere;
}
.kpi-note {
    color: #657568 !important;
    font-size: 11px;
    margin-top: 8px;
}

/* Grafik */
div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E0E4DA;
    border-radius: 16px;
    padding: 8px;
}

/* Radio dan keterangan */
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] p,
div[data-testid="stRadio"] label span {
    color: #26352C !important;
}
div[data-testid="stCaptionContainer"] p {
    color: #526358 !important;
}

/* Insight */
.insight-card {
    background: #E8EEE4;
    border-left: 4px solid #4F6B50;
    border-radius: 10px;
    padding: 14px 16px;
    margin: 11px 0;
    color: #26352C !important;
    font-size: 13px;
    line-height: 1.65;
}
.insight-card b {
    color: #203B2C !important;
}
.footer {
    text-align: center;
    color: #657568 !important;
    font-size: 11px;
    padding: 18px 8px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
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

# =========================================================
# MEMBACA EXCEL
# =========================================================
EXCEL_FILE = "Data_Simulasi_Penjualan_Gudeg_Jogja_2025.xlsx"

try:
    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="Data_Penjualan")
    except ValueError:
        df = pd.read_excel(EXCEL_FILE, sheet_name=0)

    df.columns = df.columns.astype(str).str.strip()

    required_columns = [
        "Tanggal", "Jenis_Hari", "Outlet", "Kanal_Penjualan",
        "Jumlah_Transaksi", "Omzet_Bersih_Rp",
        "Rating_Rata_rata", "Jumlah_Ulasan"
    ]

    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        st.error(
            "Kolom berikut tidak ditemukan: "
            + ", ".join(missing_columns)
        )
        st.stop()

    # =====================================================
    # PEMBERSIHAN DATA
    # =====================================================
    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"], errors="coerce", dayfirst=True
    )

    numeric_columns = [
        "Jumlah_Transaksi", "Omzet_Bersih_Rp",
        "Rating_Rata_rata", "Jumlah_Ulasan"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["Outlet", "Kanal_Penjualan", "Jenis_Hari"]:
        df[col] = df[col].astype("string").str.strip()

    df = df.dropna(subset=["Tanggal"]).copy()
    df["Jumlah_Transaksi"] = df["Jumlah_Transaksi"].fillna(0)
    df["Omzet_Bersih_Rp"] = df["Omzet_Bersih_Rp"].fillna(0)
    df["Jumlah_Ulasan"] = df["Jumlah_Ulasan"].fillna(0)

    if df.empty:
        st.error("Tidak ada data dengan tanggal yang valid.")
        st.stop()

    # =====================================================
    # FILTER SIDEBAR
    # =====================================================
    st.sidebar.markdown(
        "<div style='background:#314C39;border:1px solid #8FA58A;"
        "border-radius:12px;padding:13px 15px;margin-bottom:12px'>"
        "<div style='color:#FFFFFF!important;font-size:23px;"
        "font-weight:700'>Pusat Filter</div>"
        "<div style='color:#E2EBDD!important;font-size:13px;"
        "margin-top:5px'>Pilih data yang ingin dianalisis.</div>"
        "</div>",
        unsafe_allow_html=True
    )

    outlet_options = sorted(df["Outlet"].dropna().unique().tolist())
    channel_options = sorted(df["Kanal_Penjualan"].dropna().unique().tolist())
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
        st.warning(
            "Tidak ada data sesuai filter. Silakan ubah pilihan filter."
        )
        st.stop()

    # =====================================================
    # FUNGSI FORMAT
    # =====================================================
    def rupiah(value):
        return "Rp " + f"{value:,.0f}".replace(",", ".")

    # =====================================================
    # KPI
    # =====================================================
    revenue = data["Omzet_Bersih_Rp"].sum()
    transactions = data["Jumlah_Transaksi"].sum()
    average_transaction = revenue / transactions if transactions > 0 else 0

    rating_data = data[
        data["Rating_Rata_rata"].notna()
        & (data["Jumlah_Ulasan"] > 0)
    ]

    total_reviews = rating_data["Jumlah_Ulasan"].sum()
    weighted_rating = (
        (
            rating_data["Rating_Rata_rata"]
            * rating_data["Jumlah_Ulasan"]
        ).sum() / total_reviews
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

    kpi_columns = st.columns(4)
    kpi_data = [
        ("Omzet Bersih", rupiah(revenue),
         "Total pendapatan setelah diskon"),
        ("Jumlah Transaksi",
         f"{transactions:,.0f}".replace(",", "."),
         "Total transaksi terpilih"),
        ("Rata-rata Nilai Transaksi", rupiah(average_transaction),
         "Omzet dibagi jumlah transaksi"),
        ("Rating Berbobot", f"{weighted_rating:.2f} / 5",
         "Dibobot berdasarkan jumlah ulasan")
    ]

    for col, (label, value, note) in zip(kpi_columns, kpi_data):
        with col:
            st.markdown(
                f'<div class="kpi-card">'
                f'<div class="kpi-label">{label}</div>'
                f'<div class="kpi-value">{value}</div>'
                f'<div class="kpi-note">{note}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    chart_font = dict(
        family="DM Sans, sans-serif", size=12, color=TEXT
    )
    chart_config = {"displayModeBar": False, "responsive": True}

    # =====================================================
    # TREN OMZET
    # =====================================================
    st.markdown(
        '<div class="section-title">Tren Omzet Bersih</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Pantau perubahan omzet berdasarkan waktu.</div>',
        unsafe_allow_html=True
    )

    period_choice = st.radio(
        "Kelompokkan tren berdasarkan",
        ["Bulanan", "Mingguan"],
        horizontal=True,
        label_visibility="visible"
    )

    trend = data.copy()

    if period_choice == "Bulanan":
        trend["Periode"] = (
            trend["Tanggal"].dt.to_period("M").dt.to_timestamp()
        )
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
        trend,
        x="Label",
        y="Omzet_Bersih_Rp",
        markers=True,
        labels={
            "Label": "Periode",
            "Omzet_Bersih_Rp": "Omzet Bersih (Rp)"
        }
    )

    trend_values = trend["Omzet_Bersih_Rp"].tolist()
    trend_max = max(trend_values)
    trend_min = min(trend_values)
    trend_middle = [BLUE, YELLOW]
    trend_marker_colors = []

    for i, value in enumerate(trend_values):
        if value == trend_max:
            trend_marker_colors.append("#238636")
        elif value == trend_min:
            trend_marker_colors.append(RED)
        else:
            trend_marker_colors.append(trend_middle[i % len(trend_middle)])

    fig_trend.update_traces(
        line=dict(color=BLUE, width=3),
        fillcolor="rgba(84,125,138,0.18)",
        marker=dict(
            size=[
                13 if value in (trend_max, trend_min) else 8
                for value in trend_values
            ],
            color=trend_marker_colors,
            line=dict(color="#FFFFFF", width=1.5)
        ),
        hovertemplate="<b>%{x}</b><br>Omzet: Rp %{y:,.0f}<extra></extra>"
    )

    if len(trend):
        max_row = trend.loc[trend["Omzet_Bersih_Rp"].idxmax()]
        min_row = trend.loc[trend["Omzet_Bersih_Rp"].idxmin()]

        fig_trend.add_annotation(
            x=max_row["Label"],
            y=max_row["Omzet_Bersih_Rp"],
            text="TERTINGGI",
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-35,
            font=dict(color="#176B2C", size=10),
            bgcolor="#E4F5E8",
            bordercolor="#238636",
            borderwidth=1
        )

        if min_row["Label"] != max_row["Label"]:
            fig_trend.add_annotation(
                x=min_row["Label"],
                y=min_row["Omzet_Bersih_Rp"],
                text="TERENDAH",
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=35,
                font=dict(color="#A61B1B", size=10),
                bgcolor="#FDE8E7",
                bordercolor=RED,
                borderwidth=1
            )

    fig_trend.update_layout(
        height=390,
        margin=dict(l=20, r=20, t=25, b=25),
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font=chart_font,
        title_font=dict(color=TEXT),
        xaxis_title="Periode",
        yaxis_title="Omzet Bersih (Rp)",
        hoverlabel=dict(bgcolor="#FFFFFF", font=dict(color=TEXT))
    )
    fig_trend.update_xaxes(
        color=TEXT,
        title_font=dict(color=TEXT),
        tickfont=dict(color=MUTED, size=11),
        showgrid=False,
        automargin=True
    )
    fig_trend.update_yaxes(
        color=TEXT,
        title_font=dict(color=TEXT),
        tickfont=dict(color=MUTED, size=11),
        gridcolor=GRID,
        zerolinecolor=GRID,
        tickformat="~s"
    )
    st.plotly_chart(fig_trend, use_container_width=True, config=chart_config)

    # =====================================================
    # PERBANDINGAN OUTLET DAN KANAL
    # =====================================================
    st.markdown(
        '<div class="section-title">Perbandingan Kinerja</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Bandingkan omzet antar-outlet dan kanal penjualan.</div>',
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

    left, right = st.columns(2)

    with left:
        fig_outlet = px.bar(
            outlet_sales,
            x="Omzet_Bersih_Rp",
            y="Outlet",
            orientation="h",
            text="Omzet_Bersih_Rp",
            title="Kinerja per Outlet",
            labels={
                "Outlet": "Outlet",
                "Omzet_Bersih_Rp": "Omzet Bersih (Rp)"
            }
        )

        rank_palette = [RED, YELLOW, BLUE, "#238636"]
        outlet_colors = [
            rank_palette[
                round(i * (len(rank_palette) - 1)
                      / max(len(outlet_sales) - 1, 1))
            ]
            for i in range(len(outlet_sales))
        ]

        fig_outlet.update_traces(
            marker_color=outlet_colors,
            marker_line_color="#FFFFFF",
            marker_line_width=1.2,
            texttemplate="%{x:,.0f}",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Omzet: Rp %{x:,.0f}<br>"
                "Posisi: %{customdata}<extra></extra>"
            ),
            customdata=[
                "TERENDAH" if i == 0
                else "TERTINGGI" if i == len(outlet_sales) - 1
                else "MENENGAH"
                for i in range(len(outlet_sales))
            ]
        )
        fig_outlet.update_layout(
            height=380,
            margin=dict(l=20, r=90, t=60, b=35),
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            showlegend=False,
            font=chart_font,
            title_font=dict(size=16, color=TEXT),
            hoverlabel=dict(bgcolor="#FFFFFF", font=dict(color=TEXT))
        )
        fig_outlet.update_xaxes(
            color=TEXT,
            tickfont=dict(color=MUTED),
            gridcolor=GRID,
            title_font=dict(color=TEXT),
            tickformat="~s"
        )
        fig_outlet.update_yaxes(
            color=TEXT,
            tickfont=dict(color=TEXT),
            title_font=dict(color=TEXT),
            showgrid=False,
            automargin=True
        )
        st.plotly_chart(
            fig_outlet, use_container_width=True, config=chart_config
        )

    with right:
        fig_channel = px.bar(
            channel_sales,
            x="Omzet_Bersih_Rp",
            y="Kanal_Penjualan",
            orientation="h",
            text="Omzet_Bersih_Rp",
            title="Kinerja per Kanal Penjualan",
            labels={
                "Kanal_Penjualan": "Kanal Penjualan",
                "Omzet_Bersih_Rp": "Omzet Bersih (Rp)"
            }
        )

        rank_palette = [RED, YELLOW, BLUE, "#238636"]
        channel_colors = [
            rank_palette[
                round(i * (len(rank_palette) - 1)
                      / max(len(channel_sales) - 1, 1))
            ]
            for i in range(len(channel_sales))
        ]

        fig_channel.update_traces(
            marker_color=channel_colors,
            marker_line_color="#FFFFFF",
            marker_line_width=1.2,
            texttemplate="%{x:,.0f}",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Omzet: Rp %{x:,.0f}<br>"
                "Posisi: %{customdata}<extra></extra>"
            ),
            customdata=[
                "TERENDAH" if i == 0
                else "TERTINGGI" if i == len(channel_sales) - 1
                else "MENENGAH"
                for i in range(len(channel_sales))
            ]
        )
        fig_channel.update_layout(
            height=380,
            margin=dict(l=20, r=90, t=60, b=35),
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            showlegend=False,
            font=chart_font,
            title_font=dict(size=16, color=TEXT),
            hoverlabel=dict(bgcolor="#FFFFFF", font=dict(color=TEXT))
        )
        fig_channel.update_xaxes(
            color=TEXT,
            tickfont=dict(color=MUTED),
            gridcolor=GRID,
            title_font=dict(color=TEXT),
            tickformat="~s"
        )
        fig_channel.update_yaxes(
            color=TEXT,
            tickfont=dict(color=TEXT),
            title_font=dict(color=TEXT),
            showgrid=False,
            automargin=True
        )
        st.plotly_chart(
            fig_channel, use_container_width=True, config=chart_config
        )

    st.markdown(
        '<div class="insight-card"><b>Keterangan warna:</b> '
        '<span style="color:#D94841;font-weight:700">Merah = terendah</span> · '
        '<span style="color:#B8860B;font-weight:700">Kuning = rendah-menengah</span> · '
        '<span style="color:#547D8A;font-weight:700">Biru = menengah-tinggi</span> · '
        '<span style="color:#238636;font-weight:700">Hijau = tertinggi</span>. '
        'Warna ditentukan dari nilai pada filter yang sedang aktif.</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # HEATMAP OMZET
    # =====================================================
    st.markdown(
        '<div class="section-title">Heatmap Omzet Penjualan</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Warna hijau semakin tua berarti omzet semakin besar. '
        'Bandingkan omzet setiap outlet berdasarkan jenis hari.</div>',
        unsafe_allow_html=True
    )

    heatmap_data = data.pivot_table(
        index="Outlet",
        columns="Jenis_Hari",
        values="Omzet_Bersih_Rp",
        aggfunc="sum",
        fill_value=0
    )

    if not heatmap_data.empty and heatmap_data.shape[1] > 0:
        # Kompatibel dengan pandas versi baru, tanpa applymap().
        heatmap_labels = heatmap_data.apply(
            lambda col: col.map(
                lambda value: f"Rp {value:,.0f}".replace(",", ".")
                if pd.notna(value) else ""
            )
        )

        fig_heatmap = px.imshow(
            heatmap_data,
            labels={
                "x": "Jenis Hari",
                "y": "Outlet",
                "color": "Omzet (Rp)"
            },
            x=heatmap_data.columns.tolist(),
            y=heatmap_data.index.tolist(),
            color_continuous_scale=[
                "#F1F7EF", "#B7D7B0", "#6FA66B", "#245B35"
            ],
            aspect="auto",
            text_auto=False
        )

        # Nilai ditampilkan langsung di setiap kotak heatmap.
        for row_i, outlet_name in enumerate(heatmap_data.index):
            for col_i, day_name in enumerate(heatmap_data.columns):
                value = heatmap_data.iloc[row_i, col_i]
                max_value = heatmap_data.to_numpy().max()

                fig_heatmap.add_annotation(
                    x=day_name,
                    y=outlet_name,
                    text=f"Rp {value:,.0f}".replace(",", "."),
                    showarrow=False,
                    font=dict(
                        color=(
                            "#FFFFFF"
                            if max_value > 0 and value >= max_value * 0.55
                            else "#203B2C"
                        ),
                        size=11
                    )
                )

        fig_heatmap.update_layout(
            height=max(320, 100 + len(heatmap_data.index) * 65),
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            font=chart_font,
            margin=dict(l=20, r=20, t=25, b=25),
            coloraxis_colorbar=dict(
                title="Omzet (Rp)",
                tickformat="~s"
            ),
            hoverlabel=dict(bgcolor=WHITE, font=dict(color=TEXT))
        )
        fig_heatmap.update_xaxes(
            side="bottom",
            tickfont=dict(color=TEXT),
            automargin=True
        )
        fig_heatmap.update_yaxes(
            autorange="reversed",
            tickfont=dict(color=TEXT),
            automargin=True
        )

        st.plotly_chart(
            fig_heatmap, use_container_width=True, config=chart_config
        )
        st.caption(
            "Cara membaca: kotak hijau tua menunjukkan omzet yang lebih tinggi. "
            "Arahkan kursor ke kotak untuk melihat nilai omzetnya."
        )
    else:
        st.info("Heatmap belum dapat dibuat karena tidak ada data untuk filter ini.")

    # =====================================================
    # POLA PENJUALAN: PIE CHART
    # =====================================================
    st.markdown(
        '<div class="section-title">Pola Penjualan</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Kontribusi omzet berdasarkan jenis hari dan insight.</div>',
        unsafe_allow_html=True
    )

    day_sales = (
        data.groupby("Jenis_Hari", as_index=False)["Omzet_Bersih_Rp"]
        .sum().sort_values("Omzet_Bersih_Rp", ascending=False)
    )

    pie_col, insight_col = st.columns([1, 1])

    with pie_col:
        pie_palette = ["#238636", BLUE, YELLOW, RED]
        pie_colors = [
            pie_palette[
                round(i * (len(pie_palette) - 1)
                      / max(len(day_sales) - 1, 1))
            ]
            for i in range(len(day_sales))
        ]
        pie_pull = [
            0.10 if i == 0
            else 0.08 if i == len(day_sales) - 1
            else 0
            for i in range(len(day_sales))
        ]

        fig_pie = px.pie(
            day_sales,
            names="Jenis_Hari",
            values="Omzet_Bersih_Rp",
            hole=0.55,
            title="Proporsi Omzet per Jenis Hari",
            color_discrete_sequence=pie_colors
        )
        fig_pie.update_traces(
            pull=pie_pull,
            marker=dict(line=dict(color="#FFFFFF", width=2)),
            textposition="inside",
            textinfo="label+percent",
            insidetextfont=dict(color="#FFFFFF", size=13),
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Omzet: Rp %{value:,.0f}<br>"
                "Kontribusi: %{percent}<extra></extra>"
            )
        )
        fig_pie.update_layout(
            height=380,
            margin=dict(l=15, r=15, t=60, b=20),
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            font=chart_font,
            title_font=dict(size=16, color=TEXT),
            legend=dict(font=dict(color=TEXT, size=12)),
            hoverlabel=dict(bgcolor="#FFFFFF", font=dict(color=TEXT))
        )
        st.plotly_chart(
            fig_pie, use_container_width=True, config=chart_config
        )

    # =====================================================
    # INSIGHT OTOMATIS
    # =====================================================
    with insight_col:
        st.markdown(
            '<div class="section-title" style="font-size:23px;">'
            'Insight Otomatis</div>',
            unsafe_allow_html=True
        )

        best_outlet = outlet_sales.iloc[-1]
        best_channel = channel_sales.iloc[-1]
        best_day = day_sales.iloc[0]

        outlet_share = (
            best_outlet["Omzet_Bersih_Rp"] / revenue * 100
            if revenue else 0
        )
        channel_share = (
            best_channel["Omzet_Bersih_Rp"] / revenue * 100
            if revenue else 0
        )
        day_share = (
            best_day["Omzet_Bersih_Rp"] / revenue * 100
            if revenue else 0
        )

        st.markdown(
            f'<div class="insight-card">'
            f'<b>Outlet dengan omzet tertinggi</b><br>'
            f'{best_outlet["Outlet"]} mencatat '
            f'{rupiah(best_outlet["Omzet_Bersih_Rp"])} '
            f'({outlet_share:.1f}% dari omzet terfilter).'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="insight-card">'
            f'<b>Kanal penjualan terkuat</b><br>'
            f'{best_channel["Kanal_Penjualan"]} mencatat '
            f'{rupiah(best_channel["Omzet_Bersih_Rp"])} '
            f'({channel_share:.1f}% dari omzet terfilter).'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="insight-card">'
            f'<b>Jenis hari dengan omzet tertinggi</b><br>'
            f'{best_day["Jenis_Hari"]} mencatat '
            f'{rupiah(best_day["Omzet_Bersih_Rp"])} '
            f'({day_share:.1f}% dari omzet terfilter).'
            f'</div>',
            unsafe_allow_html=True
        )
        st.caption("Ringkasan diperbarui otomatis berdasarkan filter.")

    # =====================================================
    # DETAIL DATA DAN DOWNLOAD
    # =====================================================
    st.markdown(
        '<div class="section-title">Detail dan Unduh Data</div>'
        '<div class="section-subtitle">'
        'Data ditampilkan sesuai filter yang sedang dipilih.</div>',
        unsafe_allow_html=True
    )

    with st.expander("Lihat detail data penjualan", expanded=True):
        detail = data.sort_values("Tanggal", ascending=False).copy()

        st.dataframe(
            detail,
            use_container_width=True,
            hide_index=True,
            height=400
        )

        st.download_button(
            "Download data terfilter (CSV)",
            data=detail.to_csv(index=False).encode("utf-8-sig"),
            file_name="data_penjualan_gudeg.csv",
            mime="text/csv"
        )

    # =====================================================
    # FOOTER
    # =====================================================
    st.markdown("---")
    st.markdown(
        f'<div class="footer">'
        f'GUDEG SEKAR ARUM · YOGYAKARTA<br>'
        f'{len(data):,} baris data setelah filter<br>'
        f'{data["Tanggal"].min():%d/%m/%Y} – '
        f'{data["Tanggal"].max():%d/%m/%Y}<br>'
        f'Sumber: file Excel dalam repository aplikasi. '
        f'Data simulasi untuk pembelajaran.'
        f'</div>',
        unsafe_allow_html=True
    )

except FileNotFoundError:
    st.error(
        f"File Excel '{EXCEL_FILE}' tidak ditemukan. "
        "Unggah file Excel ke repository yang sama dengan app.py."
    )
except Exception as error:
    st.error(
        f"Terjadi kesalahan saat membaca atau mengolah Excel: {error}"
    )
