import streamlit as st
from periodic_table_ui import render_periodic_table_with_callback
from reaction_engine import proses_reaksi
from tabel_periodik_118 import elemen_periodik

st.set_page_config(layout="wide")

st.markdown("""
    <h1 style='text-align: center;'>🧪 Penyusun Persamaan Reaksi Kimia</h1>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📌 Navigasi")
    halaman = st.radio("Pilih Halaman", ["📘 Dasar Teori", "📊 Tabel Periodik", "🧾 Info Unsur"])

if "unsur_dipilih" not in st.session_state:
    st.session_state.unsur_dipilih = []

if halaman == "📘 Dasar Teori":
    st.header("📘 Dasar Teori")
    st.write("""
        Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang
        terlibat. Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang
        terlibat. Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama
        di kedua sisi reaksi.
        
        ### 🧬 Contoh Persamaan Setara:
        [ 2H_2 + O_2 \rightarrow 2H_2O ]

        Jenis reaksi kimia umum meliputi:
        - Reaksi Kombinasi (Sintesis) 🍀
        - Reaksi Penguraian (Dekomposisi) ⚡️
        - Reaksi Pergantian Tunggal 🔁
        - Reaksi Pergantian Ganda 🔄
        - Reaksi Pembakaran 🔥

        Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
        - Jenis reaksi
        - Persamaan reaksi yang terbentuk
        - Massa molekul relatif (Mr) dari senyawa hasil reaksi
    """)

elif halaman == "📊 Tabel Periodik":
    st.header("📊 Tabel Periodik")
    st.markdown("Klik dua unsur untuk melihat reaksi kimianya.")
    
    def on_click(unsur):
        if len(st.session_state.unsur_dipilih) >= 2:
            st.session_state.unsur_dipilih = []
        st.session_state.unsur_dipilih.append(unsur)

    render_periodic_table_with_callback(elemen_periodik, on_click)

    if len(st.session_state.unsur_dipilih) == 2:
        unsur1, unsur2 = st.session_state.unsur_dipilih
        hasil = proses_reaksi(unsur1, unsur2)

        st.subheader("🔬 Hasil Reaksi: {} + {}".format(unsur1, unsur2))
        if hasil:
            st.latex(hasil["persamaan"])
            st.success(f"Jenis Reaksi: {hasil['jenis']}")
            st.info(f"Massa molekul relatif (Mr) dari {hasil['senyawa']}: {hasil['massa_molekul']}")
        else:
            st.error("Reaksi tidak ditemukan untuk kombinasi unsur ini.")

        if st.button("Reset Pilihan Unsur"):
            st.session_state.unsur_dipilih = []

elif halaman == "🧾 Info Unsur":
    st.header("🧾 Info Unsur")

    def show_info(unsur):
        data = next((e for e in elemen_periodik if e["simbol"] == unsur), None)
        if data:
            st.markdown(f"""
                ### ℹ️ {data['simbol']} - {data['nama']}
                - **Nomor Atom**: {data['nomor_atom']}
                - **Golongan**: {data['golongan']}
                - **Massa Molar**: {data['massa']} g/mol
            """)

    def on_click_unsur(unsur):
        st.session_state.unsur_dipilih_info = unsur

    render_periodic_table_with_callback(elemen_periodik, on_click_unsur)

    if "unsur_dipilih_info" in st.session_state:
        show_info(st.session_state.unsur_dipilih_info)
