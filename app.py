import streamlit as st
from reaction_engine import (
    susun_reaksi_dari_unsur, hitung_massa_molekul, identifikasi_jenis_reaksi,
    cek_penyetaraan, parse_senyawa
)
from periodic_table_ui import tampilkan_tabel_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi', layout='wide')
st.title('🔬 Penyusun Persamaan Reaksi Kimia')

st.subheader('Mode: Susun Reaksi dari Tabel Periodik')
st.caption('Klik dua unsur dari tabel periodik di bawah untuk membentuk reaksi.')

if 'selected_elements' not in st.session_state:
    st.session_state.selected_elements = []

tampilkan_tabel_periodik()

if st.button('🔁 Reset Pilihan Unsur'):
    st.session_state.selected_elements = []

unsur_terpilih = st.session_state.get('selected_elements', [])
if len(unsur_terpilih) == 2:
    hasil = susun_reaksi_dari_unsur(unsur_terpilih)
    if hasil:
        st.markdown('### Persamaan Reaksi:')
        if hasil.get('setara'):
            st.latex(hasil['setara'])
        elif hasil.get('setara_opsi'):
            for opsi in hasil['setara_opsi']:
                st.latex(opsi)

        jenis = hasil.get('jenis')
        if jenis:
            st.success(f'Jenis Reaksi: {jenis}')

        produk_akhir = hasil.get('produk') or (hasil.get('produk_opsional') or [None])[0]
        if produk_akhir:
            mr = hitung_massa_molekul(produk_akhir)
            if mr:
                st.info(f'Massa molekul relatif (Mr) dari {produk_akhir}: {mr:.2f}')

st.subheader('Mode: Masukkan Reaksi Manual')
input_reaksi = st.text_input('Masukkan reaksi kimia (contoh: HCl + NaOH → NaCl + H2O)')
if input_reaksi:
    st.latex(input_reaksi.replace('→', ' \rightarrow '))
    setara = cek_penyetaraan(input_reaksi)
    if setara:
        st.info('✔ Reaksi ini sudah setara')
    else:
        st.warning('✖ Reaksi belum setara')

    jenis = identifikasi_jenis_reaksi(input_reaksi)
    if jenis:
        st.success(f'Jenis Reaksi: {jenis}')

    produk_akhir = parse_senyawa(input_reaksi, produk=True)
    mr_produk = hitung_massa_molekul(produk_akhir)
    if mr_produk:
        st.info(f'Massa molekul produk utama: {mr_produk:.2f}')