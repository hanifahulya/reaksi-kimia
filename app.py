import streamlit as st
from reaction_engine import (
    susun_reaksi_dari_unsur,
    hitung_massa_molekul,
    identifikasi_jenis_reaksi,
    cek_penyetaraan,
    parse_senyawa,
)
from periodic_table_ui import tampilkan_tabel_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi', layout='wide')
st.title('🔬 Penyusun Persamaan Reaksi Kimia')

# Mode 1: Reaksi dari unsur
st.subheader('Mode: Susun Reaksi dari Tabel Periodik')
st.caption('Klik dua unsur dari tabel periodik di bawah untuk membentuk reaksi.')

if 'selected_elements' not in st.session_state:
    st.session_state.selected_elements = []

unsur_terpilih = st.session_state.get('selected_elements', [])

if st.button('🔁 Reset Pilihan Unsur'):
    st.session_state.selected_elements = []
    st.experimental_rerun()

tampilkan_tabel_periodik()

if len(unsur_terpilih) == 2:
    hasil = susun_reaksi_dari_unsur(unsur_terpilih)
    st.markdown('### Persamaan Reaksi:')
    if hasil:
        st.latex(hasil['setara'])
        if hasil.get('jenis'):
            st.success(f"Jenis Reaksi: {hasil['jenis']}")
        if hasil.get('setara_opsi'):
            st.markdown('**Opsi Reaksi Lain:**')
            for opsi in hasil['setara_opsi']:
                st.latex(opsi)
        produk_akhir = hasil.get('produk') or (hasil.get('produk_opsional') or [None])[0]
        if produk_akhir:
            mr = hitung_massa_molekul(produk_akhir)
            if mr:
                st.info(f'Massa molekul relatif (Mr) dari {produk_akhir}: {mr:.2f}')

# Mode 2: Cek Reaksi Manual
st.subheader('Mode: Masukkan Reaksi Manual')
input_reaksi = st.text_input('Masukkan reaksi kimia (contoh: HCl + NaOH → NaCl + H2O)')

if input_reaksi:
    st.latex(input_reaksi.replace('→', ' \\rightarrow '))
    setara = cek_penyetaraan(input_reaksi)
    if setara:
        st.info('✔ Reaksi ini sudah setara')
    else:
        st.warning('✖ Reaksi belum setara')
    
    jenis = identifikasi_jenis_reaksi(input_reaksi)
    if jenis:
        st.success(f'Jenis Reaksi: {jenis}')

    produk = parse_senyawa(input_reaksi, produk=True)
    if produk:
        mr_produk = hitung_massa_molekul(produk)
        if mr_produk:
            st.info(f'Massa molekul produk utama: {mr_produk:.2f}')
