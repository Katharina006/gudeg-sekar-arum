import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Gudeg Sekar Arum Yogyakarta",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PALET WARNA
# =========================================================
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
.stApp {
    background-color: #F4F2EA !important;
    color: #26352C !important;
}
[data-testid="stHeader"] {
    background: #F4F2EA !important;
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
    border-color: #8FA58A !important;
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

/* Filter hijau sage */
[data-testid="stSidebar"] [data-baseweb="tag"] {
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
[data-baseweb="popover"] {
    color: #26352C !important;
}
[data-baseweb="popover"] li {
    color: #26352C !important;
}

/* Input tanggal */
[data-testid="stDateInput"] label {
    color: #F7F7F0 !important;
}
[data-testid="stDateInput"] input {
    background-color: #FFFFFF !important;
    color: #26352C !important;
    -webkit-text-fill-color: #26352C !important;
    border-color: #B8C7B5 !important;
}
[data-testid="stDateInput"] button {
    background-color: #FFFFFF !important;
    color: #26352C !important;
}

/* Header */
.hero {
    background: linear-gradient(115deg, #E5EADD, #FFFDF5, #E7EBDD);
    border: 1px solid #D9E0D3;
    border-radius: 22px;
    padding: 30px 34px;
    margin-bottom: 24px;
}
.hero-title {
    color: #203B2C !important;
    font-family: Georgia, serif;
    font-size: clamp(30px, 3.5vw, 46px);
    font-weight: 700;
    margin: 0;
}
.hero-location {
    color: #238636 !important;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 5px;
    margin-top: 8px;
}
.hero-description {
    color: #526358 !important;
    font-size: 14px;
    margin-top: 12px;
}

/* Judul bagian */
.section-title {
    color: #203B2C !important;
    font-family: Georgia, serif;
    font-size: 25px;
    font-weight: 700;
    margin-top: 22px;
    margin-bottom: 4px;
}
.section-subtitle {
    color: #526358 !important;
    font-size: 13px;
    margin-bottom: 14px;
}

/* KPI */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E0E4DA;
    border-radius: 15px;
    padding: 18px;
    min-height: 128px;
}
.kpi-label {
    color: #526358 !important;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
}
.kpi-value {
    color: #203B2C !important;
    font-size: clamp(18px, 1.6vw, 25px);
    font-weight: 700;
    margin-top: 12px;
    overflow-wrap: anywhere;
}
.kpi-note {
    color: #657568 !important;
    font-size: 11px;
    margin-top: 7px;
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

/* Tabel detail */
[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
}
[data-testid="stDataFrame"] * {
    color: #26352C !important;
}

/* Tombol download */
[data-testid="stDownloadButton"] button {
    background: #314C39 !important;
    color: #FFFFFF !important;
    border: 1px solid #314C39 !important;
    border-radius: 8px !important;
}
[data-testid="stDownloadButton"] button * {
    color: #FFFFFF !important;
}

/* Radio dan teks */
[data-testid="stRadio"] label,
[data-testid="stRadio"] p {
    color: #26352C !important;
}
[data-testid="stCaptionContainer"] p {
    color: #526358 !important;
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
# BACA FILE EXCEL
# Pastikan file Excel berada satu folder dengan app.py
# =========================================================
EXCEL_FILE = "Data_Simulasi_Penjualan_Gudeg_Jogja_2025.xlsx"

try:
    try:
        df = pd.read_excel(
            EXCEL_FILE,
            sheet_name="Data_Penjualan"
        )
    except ValueError:
        df = pd.read_excel(
            EXCEL_FILE,
            sheet_name=0
        )

    df.columns = df.columns.astype(str).str.strip()

    required = [
        "Tanggal",
        "Jenis_Hari",
        "Outlet",
        "Kanal_Penjualan",
        "Jumlah_Transaksi",
        "Omzet_Bersih_Rp",
        "Rating_Rata_rata",
        "Jumlah_Ulasan"
    ]

    missing = [col for col in required if col not in df.columns]

    if missing:
        st.error(
            "Kolom Excel tidak ditemukan: " + ", ".join(missing)
        )
        st.stop()

    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"],
        errors="coerce",
        dayfirst=True
    )

    numeric_columns = [
        "Jumlah_Transaksi",
        "Omzet_Bersih_Rp",
        "Rating_Rata_rata",
        "Jumlah_Ulasan"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["Outlet", "Kanal_Penjualan", "Jenis_Hari"]:
        df[col] = df[col].astype("string").str.strip()

    df = df.dropna(subset=["Tanggal"]).copy()

    for col in [
        "Jumlah_Transaksi",
        "Omzet_Bersih_Rp",
        "Jumlah_Ulasan"
    ]:
        df[col] = df[col].fillna(0)

    if df.empty:
        st.error("Tidak ada data penjualan dengan tanggal valid.")
        st.stop()

    # =====================================================
    # SIDEBAR FILTER
    # =====================================================
    st.sidebar.markdown(
        "<h2 style='color:#F7F7F0;margin-bottom:4px'>Pusat Filter</h2>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        "<p style='color:#DCE7D8;font-size:14px;margin-top:0;"
        "margin-bottom:16px'>Pilih data yang ingin dianalisis.</p>",
        unsafe_allow_html=True
    )

    outlet_options = sorted(
        df["Outlet"].dropna().unique().tolist()
    )
    channel_options = sorted(
        df["Kanal_Penjualan"].dropna().unique().tolist()
    )
    day_options = sorted(
        df["Jenis_Hari"].dropna().unique().tolist()
    )

    selected_outlets = st.sidebar.multiselect(
        "Outlet",
        outlet_options,
        default=outlet_options
    )

    selected_channels = st.sidebar.multiselect(
        "Kanal Penjualan",
        channel_options,
        default=channel_options
    )

    selected_days = st.sidebar.multiselect(
        "Jenis Hari",
        day_options,
        default=day_options
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
        st.sidebar.error(
            "Tanggal awal tidak boleh melewati tanggal akhir."
        )
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
            "Tidak ada data sesuai filter. Ubah pilihan filter."
        )
        st.stop()

    # =====================================================
    # FUNGSI FORMAT RUPIAH
    # =====================================================
    def rupiah(value):
        return "Rp " + f"{value:,.0f}".replace(",", ".")

    # =====================================================
    # RINGKASAN KPI
    # =====================================================
    revenue = data["Omzet_Bersih_Rp"].sum()
    transactions = data["Jumlah_Transaksi"].sum()

    average_transaction = (
        revenue / transactions if transactions > 0 else 0
    )

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

    kpis = st.columns(4)

    kpi_items = [
        (
            "Omzet Bersih",
            rupiah(revenue),
            "Total pendapatan setelah diskon"
        ),
        (
            "Jumlah Transaksi",
            f"{transactions:,.0f}".replace(",", "."),
            "Total transaksi terpilih"
        ),
        (
            "Rata-rata Nilai Transaksi",
            rupiah(average_transaction),
            "Omzet dibagi jumlah transaksi"
        ),
        (
            "Rating Berbobot",
            f"{weighted_rating:.2f} / 5",
            "Dibobot berdasarkan jumlah ulasan"
        )
    ]

    for col, (label, value, note) in zip(kpis, kpi_items):
        with col:
            st.markdown(
                f'<div class="kpi-card">'
                f'<div class="kpi-label">{label}</div>'
                f'<div class="kpi-value">{value}</div>'
                f'<div class="kpi-note">{note}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    chart_font = {
        "family": "Arial, sans-serif",
        "size": 12,
        "color": TEXT
    }

    chart_config = {
        "displayModeBar": False,
        "responsive": True
    }

    # =====================================================
    # TREN OMZET
    # =====================================================
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
            + " – "
            + week_end.dt.strftime("%d %b %Y")
        )

    trend = (
        trend.groupby(
            ["Periode", "Label"],
            as_index=False
        )["Omzet_Bersih_Rp"]
        .sum()
        .sort_values("Periode")
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

    if not trend.empty:
        hi = trend["Omzet_Bersih_Rp"].idxmax()
        lo = trend["Omzet_Bersih_Rp"].idxmin()

        marker_colors = [
            GREEN if idx == hi
            else RED if idx == lo
            else BLUE
            for idx in trend.index
        ]

        marker_sizes = [
            13 if idx in (hi, lo) else 8
            for idx in trend.index
        ]

        fig_trend.update_traces(
            line=dict(color=BLUE, width=3),
            fillcolor="rgba(84,125,138,0.18)",
            marker=dict(
                size=marker_sizes,
                color=marker_colors,
                line=dict(color=CARD, width=1.5)
            ),
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Omzet: Rp %{y:,.0f}"
                "<extra></extra>"
            )
        )

        maxrow = trend.loc[hi]
        minrow = trend.loc[lo]

        fig_trend.add_annotation(
            x=maxrow["Label"],
            y=maxrow["Omzet_Bersih_Rp"],
            text="TERTINGGI",
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-35,
            font=dict(color=GREEN, size=10),
            bgcolor="#E4F5E8",
            bordercolor=GREEN,
            borderwidth=1
        )

        if hi != lo:
            fig_trend.add_annotation(
                x=minrow["Label"],
                y=minrow["Omzet_Bersih_Rp"],
                text="TERENDAH",
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=35,
                font=dict(color="#9F302B", size=10),
                bgcolor="#FCE9E7",
                bordercolor=RED,
                borderwidth=1
            )

    fig_trend.update_layout(
        height=390,
        margin=dict(l=20, r=20, t=45, b=25),
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font=chart_font,
        hoverlabel=dict(
            bgcolor=CARD,
            font=dict(color=TEXT)
        )
    )

    fig_trend.update_xaxes(
        color=TEXT,
        tickfont=dict(color=MUTED),
        showgrid=False,
        automargin=True
    )

    fig_trend.update_yaxes(
        color=TEXT,
        tickfont=dict(color=MUTED),
        gridcolor=GRID,
        tickformat="~s"
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True,
        config=chart_config
    )

    # =====================================================
    # PERBANDINGAN OUTLET DAN KANAL
    # =====================================================
    st.markdown(
        '<div class="section-title">Perbandingan Kinerja</div>'
        '<div class="section-subtitle">'
        'Merah = terendah, kuning dan biru = nilai menengah, '
        'hijau = tertinggi.</div>',
        unsafe_allow_html=True
    )

    outlet_sales = (
        data.groupby("Outlet", as_index=False)["Omzet_Bersih_Rp"]
        .sum()
        .sort_values("Omzet_Bersih_Rp", ascending=True)
    )

    channel_sales = (
        data.groupby(
            "Kanal_Penjualan",
            as_index=False
        )["Omzet_Bersih_Rp"]
        .sum()
        .sort_values("Omzet_Bersih_Rp", ascending=True)
    )

    rank_palette = [RED, YELLOW, BLUE, GREEN]

    def rank_colors(n):
        if n <= 0:
            return []
        if n == 1:
            return [GREEN]
        return [
            rank_palette[
                round(i * (len(rank_palette) - 1) / (n - 1))
            ]
            for i in range(n)
        ]

    c1, c2 = st.columns(2)

    for container, sales, category, title in [
        (
            c1,
            outlet_sales,
            "Outlet",
            "Kinerja per Outlet"
        ),
        (
            c2,
            channel_sales,
            "Kanal_Penjualan",
            "Kinerja per Kanal Penjualan"
        )
    ]:
        with container:
            fig = px.bar(
                sales,
                x="Omzet_Bersih_Rp",
                y=category,
                orientation="h",
                text="Omzet_Bersih_Rp",
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
                marker_line_color=CARD,
                marker_line_width=1.2,
                texttemplate="%{x:,.0f}",
                textposition="outside",
                cliponaxis=False,
                customdata=positions,
                hovertemplate=(
                    "<b>%{y}</b><br>"
                    "Omzet: Rp %{x:,.0f}<br>"
                    "Posisi: %{customdata}"
                    "<extra></extra>"
                )
            )

            fig.update_layout(
                height=380,
                margin=dict(l=20, r=90, t=60, b=35),
                paper_bgcolor=CARD,
                plot_bgcolor=CARD,
                showlegend=False,
                font=chart_font,
                title_font=dict(size=16, color=TEXT),
                hoverlabel=dict(
                    bgcolor=CARD,
                    font=dict(color=TEXT)
                )
            )

            fig.update_xaxes(
                color=TEXT,
                tickfont=dict(color=MUTED),
                gridcolor=GRID,
                tickformat="~s"
            )

            fig.update_yaxes(
                color=TEXT,
                tickfont=dict(color=TEXT),
                showgrid=False,
                automargin=True
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config=chart_config
            )

    st.markdown(
        f'<div class="insight-card"><b>Keterangan warna:</b> '
        f'<span style="color:{RED};font-weight:700">'
        f'Merah = terendah</span> · '
        f'<span style="color:#A77B00;font-weight:700">'
        f'Kuning = rendah-menengah</span> · '
        f'<span style="color:{BLUE};font-weight:700">'
        f'Biru = menengah-tinggi</span> · '
        f'<span style="color:{GREEN};font-weight:700">'
        f'Hijau = tertinggi</span>. '
        f'Warna mengikuti nilai setelah filter diterapkan.</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # HEATMAP OMZET PENJUALAN
    # =====================================================
    st.markdown(
        '<div class="section-title">Heatmap Omzet Penjualan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Warna hijau semakin tua berarti omzet semakin besar. '
        'Bandingkan omzet setiap outlet berdasarkan jenis hari.'
        '</div>',
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
                "#F1F7EF",
                "#B7D7B0",
                "#6FA66B",
                "#245B35"
            ],
            aspect="auto"
        )

        max_value = heatmap_data.to_numpy().max()

        for row_i, outlet_name in enumerate(heatmap_data.index):
            for col_i, day_name in enumerate(heatmap_data.columns):
                value = heatmap_data.iloc[row_i, col_i]

                label_color = (
                    CARD
                    if max_value > 0 and value >= max_value * 0.55
                    else DARK
                )

                fig_heatmap.add_annotation(
                    x=day_name,
                    y=outlet_name,
                    text=rupiah(value),
                    showarrow=False,
                    font=dict(
                        color=label_color,
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
            hoverlabel=dict(
                bgcolor=CARD,
                font=dict(color=TEXT)
            )
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
            fig_heatmap,
            use_container_width=True,
            config=chart_config
        )

        st.caption(
            "Cara membaca: kotak hijau tua menunjukkan omzet yang lebih "
            "tinggi. Arahkan kursor ke kotak untuk melihat nilai omzet."
        )

        highest_position = heatmap_data.stack().idxmax()
        lowest_position = heatmap_data.stack().idxmin()
        highest_value = heatmap_data.max().max()
        lowest_value = heatmap_data.min().min()

        high_col, low_col = st.columns(2)

        with high_col:
            st.markdown(
                f'<div class="insight-card">'
                f'<b>Omzet tertinggi pada heatmap</b><br>'
                f'Outlet: {highest_position[0]}<br>'
                f'Jenis hari: {highest_position[1]}<br>'
                f'<b>{rupiah(highest_value)}</b></div>',
                unsafe_allow_html=True
            )

        with low_col:
            st.markdown(
                f'<div class="insight-card">'
                f'<b>Omzet terendah pada heatmap</b><br>'
                f'Outlet: {lowest_position[0]}<br>'
                f'Jenis hari: {lowest_position[1]}<br>'
                f'<b>{rupiah(lowest_value)}</b></div>',
                unsafe_allow_html=True
            )

    else:
        st.info(
            "Heatmap belum dapat dibuat karena tidak ada data "
            "untuk filter yang dipilih."
        )

    # =====================================================
    # POLA PENJUALAN DAN INSIGHT
    # =====================================================
    st.markdown(
        '<div class="section-title">Pola Penjualan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Kontribusi omzet berdasarkan jenis hari dan insight otomatis.'
        '</div>',
        unsafe_allow_html=True
    )

    day_sales = (
        data.groupby(
            "Jenis_Hari",
            as_index=False
        )["Omzet_Bersih_Rp"]
        .sum()
        .sort_values("Omzet_Bersih_Rp", ascending=False)
    )

    pie_col, insight_col = st.columns([1, 1])

    with pie_col:
        pie_palette = [GREEN, BLUE, YELLOW, RED]

        pie_colors = [
            pie_palette[
                round(
                    i * (len(pie_palette) - 1)
                    / max(len(day_sales) - 1, 1)
                )
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
            marker=dict(
                line=dict(color=CARD, width=2)
            ),
            textposition="inside",
            textinfo="label+percent",
            insidetextfont=dict(color=TEXT, size=12),
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Omzet: Rp %{value:,.0f}<br>"
                "Kontribusi: %{percent}"
                "<extra></extra>"
            )
        )

        fig_pie.update_layout(
            height=380,
            margin=dict(l=15, r=15, t=60, b=20),
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            font=chart_font,
            title_font=dict(size=16, color=TEXT),
            legend=dict(
                font=dict(color=TEXT, size=12)
            ),
            hoverlabel=dict(
                bgcolor=CARD,
                font=dict(color=TEXT)
            )
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True,
            config=chart_config
        )

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
            f'{best_outlet["Outlet"]}: '
            f'{rupiah(best_outlet["Omzet_Bersih_Rp"])} '
            f'({outlet_share:.1f}% dari omzet terfilter).</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="insight-card">'
            f'<b>Outlet dengan omzet terendah</b><br>'
            f'{worst_outlet["Outlet"]}: '
            f'{rupiah(worst_outlet["Omzet_Bersih_Rp"])}.</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="insight-card">'
            f'<b>Kanal penjualan tertinggi / terendah</b><br>'
            f'{best_channel["Kanal_Penjualan"]}: '
            f'{rupiah(best_channel["Omzet_Bersih_Rp"])} · '
            f'{worst_channel["Kanal_Penjualan"]}: '
            f'{rupiah(worst_channel["Omzet_Bersih_Rp"])}.</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="insight-card">'
            f'<b>Jenis hari dengan omzet tertinggi</b><br>'
            f'{best_day["Jenis_Hari"]}: '
            f'{rupiah(best_day["Omzet_Bersih_Rp"])} '
            f'({day_share:.1f}% dari omzet terfilter).</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Ringkasan diperbarui otomatis berdasarkan filter."
        )

    # =====================================================
    # DETAIL DATA PENJUALAN DAN DOWNLOAD
    # =====================================================
    st.markdown(
        '<div class="section-title">Lihat Detail Data Penjualan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Data mengikuti filter outlet, kanal penjualan, jenis hari, '
        'dan rentang tanggal yang dipilih.</div>',
        unsafe_allow_html=True
    )

    detail = data.sort_values(
        "Tanggal",
        ascending=False
    ).copy()

    st.dataframe(
        detail,
        use_container_width=True,
        hide_index=True,
        height=400
    )

    st.download_button(
        label="Download Data Penjualan (CSV)",
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
        "Unggah file Excel ke repository GitHub yang sama dengan app.py."
    )

except Exception as error:
    st.error(
        f"Terjadi kesalahan saat membaca atau mengolah Excel: {error}"
    )
