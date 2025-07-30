import streamlit as st
from periodic_table_ui import render_periodic_table
from reaction_engine import proses_reaksi
from tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.markdown("<h1 style='font-size: 38px;'>🧪 Penyusun Persamaan Reaksi Kimia</h1>", unsafe_allow_html=True)

# Sidebar navigasi
st.sidebar.markdown("### 📌 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["📘 Dasar Teori", "📊 Tabel Periodik", "🔍 Info Unsur"], label_visibility="collapsed")

# Halaman Dasar Teori
if "Dasar Teori" in halaman:
    st.markdown("## 📘 Dasar Teori")
    st.write("""
    Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang terlibat.
    Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang terlibat.
    Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.
    """)

    st.markdown("### 🔮 Contoh Persamaan Setara: `[ 2H_2 + O_2 \\rightarrow 2H_2O ]`")

    st.markdown("#### Jenis reaksi kimia umum meliputi:")
    st.markdown("- Reaksi Kombinasi (Sintesis) ☘️")
    st.markdown("- Reaksi Penguraian (Dekomposisi) ⚡")
    st.markdown("- Reaksi Pergantian Tunggal 🧩")
    st.markdown("- Reaksi Pergantian Ganda 🧬")
    st.markdown("- Reaksi Pembakaran 🔥")

    st.write("Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:")
    st.markdown("- Persamaan reaksi setara")
    st.markdown("- Jenis reaksi")
    st.markdown("- Massa molekul relatif (Mr) senyawa hasil reaksi")

# Halaman Tabel Periodik & Reaksi
elif "Tabel Periodik" in halaman:
    st.markdown("## 📊 Tabel Periodik Interaktif")

    selected_elements = render_periodic_table(elemen_periodik)

    if len(selected_elements) == 2:
        unsur1, unsur2 = selected_elements
        hasil = proses_reaksi(unsur1, unsur2)

        if hasil:
            st.markdown("## 🧪 Persamaan Reaksi:")
            st.latex(hasil["persamaan"])
            st.success(f"Jenis Reaksi: {hasil['jenis']}")
            st.info(f"Massa molekul relatif (Mr) dari {hasil['produk']}: {hasil['massa_molar']}")
        else:
            st.warning("Reaksi tidak ditemukan untuk kombinasi unsur ini.")

    elif len(selected_elements) == 1:
        st.info("Pilih satu unsur lagi untuk menampilkan hasil reaksi.")
    else:
        st.info("Klik dua unsur untuk melihat kemungkinan reaksinya.")

# Halaman Info Unsur
elif "Info Unsur" in halaman:
    st.markdown("## 🔍 Informasi Unsur")

    selected_symbol = st.selectbox("Pilih Unsur", sorted([el["simbol"] for el in elemen_periodik]))

    data_unsur = next((el for el in elemen_periodik if el["simbol"] == selected_symbol), None)

    if data_unsur:
        st.markdown(f"### ⚗️ Info Unsur: {selected_symbol}")
        st.markdown(f"**Nama:** {data_unsur.get('nama', '-')}")
        st.markdown(f"**Nomor Atom:** {data_unsur.get('nomor_atom', '-')}")
        st.markdown(f"**Golongan:** {data_unsur.get('golongan', '-')}")
        st.markdown(f"**Massa Molar (Ar):** {data_unsur.get('massa', '-')} g/mol")
        st.markdown(f"**Status:** {data_unsur.get('status', '-')}")
        st.markdown(f"**Deskripsi:** {data_unsur.get('deskripsi', '-')}")
