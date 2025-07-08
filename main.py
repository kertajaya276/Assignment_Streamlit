import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Portofolio Saya as Data Scientist")
st.header("People Analytic")
st.image('https://www.enterpriseappstoday.com/wp-content/uploads/2022/08/Job-Satisfaction-Statistics.jpg', width=600)
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Analisis", "Kontak"])

if page == 'Kontak':
    import kontak
    kontak.tampilkan_kontak()
elif page == 'Tentang Saya':
    import tentang
    tentang.tampilkan_tentang()
elif page == 'Analisis':
    import analisis
    analisis.tampilkan_analisis()
