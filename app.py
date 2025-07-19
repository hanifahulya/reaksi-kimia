    hasil = susun_reaksi_dari_unsur(unsur_terpilih)
    st.markdown('### Persamaan Reaksi:')
unsur_terpilih = st.session_state.get('selected_elements', [])
else:
        mr = hitung_massa_molekul(produk_akhir)
    setara = cek_penyetaraan(input_reaksi)
import streamlit as st
            st.info(f'Massa molekul relatif (Mr) dari {produk_akhir}: {mr:.2f}')
st.title('🔬 Penyusun Persamaan Reaksi Kimia')
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul, identifikasi_jenis_reaksi, cek_penyetaraan, parse_senyawa
st.set_page_config(page_title='Penyusun Persamaan Reaksi', layout='wide')
st.subheader('Mode: Susun Reaksi dari Tabel Periodik')
    mr_produk = hitung_massa_molekul(parse_senyawa(input_reaksi, produk=True))
        st.latex(hasil['setara'])
from periodic_table_ui import tampilkan_tabel_periodik
    if jenis: st.success(f'Jenis Reaksi: {jenis}')
if st.button('🔁 Reset Pilihan Unsur'):
    jenis = identifikasi_jenis_reaksi(input_reaksi)
    if hasil.get('jenis'):
st.caption('Klik dua unsur dari tabel periodik di bawah untuk membentuk reaksi.')
input_reaksi = st.text_input('Masukkan reaksi kimia (contoh: HCl + NaOH → NaCl + H2O)')
    else: st.warning('✖ Reaksi belum setara')
        st.success(f'Jenis Reaksi: {hasil['jenis']}')
if input_reaksi:
tampilkan_tabel_periodik()
            st.latex(opsi)
if len(unsur_terpilih) == 2:
    hasil = None
    elif hasil.get('setara_opsi'):
        if mr:
    if setara: st.info('✔ Reaksi ini sudah setara')
    if produk_akhir:
if hasil:
st.subheader('Mode: Masukkan Reaksi Manual')
if 'selected_elements' not in st.session_state:
    produk_akhir = hasil.get('produk') or (hasil.get('produk_opsional') or [None])[0]
    st.session_state.selected_elements = []
        for opsi in hasil['setara_opsi']:
    if hasil.get('setara'):
    st.latex(input_reaksi.replace('→', ' 
ightarrow '))
    if mr_produk: st.info(f'Massa molekul produk utama: {mr_produk:.2f}')
