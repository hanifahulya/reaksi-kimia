import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik, tampilkan_tabel_info_unsur
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from utils.tabel_periodik_118 import Ar_tiap_unsur

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.title("🧪 Penyusun Persamaan Reaksi Kimia")

# Sidebar Navigasi
with st.sidebar:
    st.markdown("### 📌 Navigasi")
    halaman = st.radio("Pilih Halaman", ["📘 Dasar Teori", "🔬 Tabel Periodik", "🔎 Info Unsur"], label_visibility="collapsed")

# Halaman Dasar Teori
if "Dasar Teori" in halaman:
    st.header("📘 Dasar Teori")
    st.markdown("""
    Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang terlibat. 
    Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang terlibat. Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.

    🧬 **Contoh Persamaan Setara:**  
    \\[ 2H_2 + O_2 \\rightarrow 2H_2O \\]

    Jenis reaksi kimia umum meliputi:
    - Reaksi Kombinasi (Sintesis) 🧩
    - Reaksi Penguraian (Dekomposisi) ⚡
    - Reaksi Pergantian Tunggal 🔁
    - Reaksi Pergantian Ganda 🔄
    - Reaksi Pembakaran 🔥

    Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
    - Persamaan reaksi setara
    - Jenis reaksi ⚗️
    - Berat molekul (BM) senyawa hasil reaksi dalam satuan **g/mol** ⚖️
    """)

# Halaman Tabel Periodik Interaktif
elif "Tabel Periodik" in halaman:
    st.header("🔬 Tabel Periodik Unsur")

    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", 
                              options=["Semua", "logam alkali", "logam alkali tanah", "logam transisi", 
                                       "logam pasca transisi", "metaloid", "nonlogam", "halogen", 
                                       "gas mulia", "lanthanida", "aktinida"])

    tampilkan_tabel_periodik(
        filter_golongan=gol_filter if gol_filter != "Semua" else None,
        dengan_warna=True
    )

    if "selected_elements" in st.session_state and len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        st.subheader(f"🔍 Hasil Reaksi: {unsur1} + {unsur2}")
        hasil = susun_reaksi_dari_unsur([unsur1, unsur2])
        if hasil:
            st.subheader("📄 Persamaan Reaksi:")
            st.latex(hasil["setara"] if "setara" in hasil else hasil["setara_opsi"][0])
            st.success(f"Jenis Reaksi: {hasil['jenis']}")
            produk = hasil.get("produk", hasil.get("produk_opsional", ["?"])[0])
            bm = hitung_massa_molekul(produk)
            if bm:
                st.info(f"Massa molekul relatif (Mr) dari {produk}: {round(bm, 2)}")
        else:
            st.warning("Tidak ditemukan reaksi yang cocok antara kedua unsur ini.")
        if st.button("🔁 Reset Pilihan"):
            st.session_state.selected_elements = []

# Halaman Info Unsur
elif "Info Unsur" in halaman:
    st.header("🔎 Informasi Unsur Kimia")
    tampilkan_tabel_info_unsur()
