import streamlit as st

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
tulisan_css='''
<style>
    .stTabs p{
        color:blue;
        font-family:"comic sans ms";
        font-size:20px;
        font-weight:bold;
        padding:5px;
    }
    .stTabs p:hover{
        background-color:black;
        color:yellow;
    }
    .stTabs p:active{
        background-color:red;
        color:green;
    }
</style>
'''
st.markdown(tulisan_css,unsafe_allow_html=True)

tab = st.tabs(["Ayo Membaca","Latihan"])
with tab[0]:
# Judul dengan animasi warna
    st.markdown("""
<style>
.dynamic-color-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    font-family:broadway;
    color: #ff6347;
    animation: colorChange 4s infinite;
}

@keyframes colorChange {
    0% { color: #ff6347; }
    25% { color: #1e90ff; }
    50% { color: #32cd32; }
    75% { color: #ffa500; }
    100% { color: #ff6347; }
}
#latihan{
    font-family:"bauhaus 93";
    color:green;
    text-shadow:2px 2px 2px red
}
.stTextInput p{
    font-family:"brush script mt";
    color:purple;
    font-size:20px;
}
#text_input_1, #text_input_2, #text_input_3{
    border:2px solid black;
    border-radius:10px;
}
#text_input_1:hover, #text_input_2:hover, #text_input_3:hover{
    background-color:yellow;
}
#text_input_1:focus, #text_input_2:focus, #text_input_3:focus{
    background-color:orange;
}
.e115fcil0{
    font-family:arial;
    font-size:15px;
    font-weight:bold;
    color:black;
}
.paragraf{
    font-family:Arial;
    font-size:20px;
    padding:5px;
    border:2px solid black;
    border-radius:10px;
    text-indent:60px;
    margin:10px;
    text-align:justify;
}
.paragraf:hover{
    background-color:yellow;
}
</style>
<div class="dynamic-color-title">Sayur dan Buah Bukan Sekadar Pelengkap Makan</div>
""", unsafe_allow_html=True)
    kolom1 = st.columns(3,vertical_alignment="center")
    with kolom1[0]:
        st.image("https://media0.giphy.com/media/oUoFkpVlKANM5Rapya/giphy.gif?cid=6c09b952wz1prolr8a1feq930ktl824wb55rjr53vpay0h26&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s",width=200,caption="Sayur-sayuran")
    with kolom1[1]:
        st.image("https://cdn.pixabay.com/photo/2013/07/13/01/22/vegetables-155616_960_720.png",width=200)
    with kolom1[2]:
        st.image("https://i.pinimg.com/originals/a6/eb/d4/a6ebd40a3e5d42f314d50dc0eb27aa02.gif",width=150,caption="buah-buahan")
    st.markdown('''<div class="paragraf">Sayur asem, sayur labu, sayur nangka. Menu ini memang mengandung kata “sayur”  di dalamnya, tetapi seringkali
hanya mengandung sedikit sekali jenis sayuran. Bagi sebagian masyarakat Indonesia, sayur dan buah masih dianggap sebagai pelengkap
makan yang kerap hanya menjadi “hiasan” dengan porsi saji yang sedikit. Nasi dan lauk saja sudah dianggap cukup, yang penting kenyang,
padahal itu masih kurang. Inilah yang membuat kurangnya konsumsi sayur dan buah di Indonesia</div>''',unsafe_allow_html=True)
    st.markdown('''<div class="paragraf">Faktanya, masyarakat Indonesia memang kurang mengonsumsi sayur dan buah. Berdasarkan data Departemen Pertanian tahun 2013,
masyarakat Indonesia baru makan sayuran sebanyak 40,35 kg/tahun, sedangkan untuk buah baru sekitar 34,55 kg/tahun. Bandingkan dengan rekomendasi badan
Perserikatan Bangsa Bangsa (PBB), yaitu konsumsi sayuran idealnya 91,25 kg/tahun dan buah 73 kg/ tahun</div>''',unsafe_allow_html=True)
    st.markdown('''<div class="paragraf">Mengonsumsi cukup sayur dan buah adalah satu cara untuk membentengi diri dari penyakit. Sayur dan buah dibutuhkan untuk
mencukupi kebutuhan tubuh akan  zat gizi penting, yaitu serat, vitamin, mineral, enzim pencernaan, dan air, yang tidak dapat ditemukan secara keseluruhan di
produk makanan lain.</div>''',unsafe_allow_html=True)
    st.markdown('''<div class="paragraf">Sayur dan buah memiliki peran penting bagi kesehatan tubuh. Serat yang dikandung sayur dan buah bermanfaat untuk kesehatan
saluran pencernaan, membantu menjaga kadar lemak, dan membantu membuat rasa kenyang. Kandungan vitamin dari buah dan sayur dengan warna yang berbeda juga menjaga
kesehatan setiap anggota tubuh, seperti mencegah sariawan, dan menjaga kesehatan mata</div>''',unsafe_allow_html=True)
    st.markdown('''<div class="paragraf">Kandungan antioksidan dalam sayur dan buah berwarna ungu berperan mencegah kerusakan sel yang menyebabkan penuaan dini, memicu kanker dan penyakit
jantung, mencegah banyak penyakit, seperti penyakit pencernaan, kencing manis, hiperkolesterol, obesitas/kegemukan, dan penyakit lainnya.
</div>''',unsafe_allow_html=True)
    st.markdown('''<div class="paragraf">Badan kesehatan PBB (WHO) merekomendasikan 400 gram buah dan sayur perhari atau 4,5 mangkuk dari berbagai jenis buah
dan sayur per hari. UU Kesehatan merekomendasikan 3-5 porsi sayur dan 2-3 porsi buah. Karena kandungan gizi dalam setiap buah tidak sama, maka disarankan
untuk makan beragam buah untuk meningkatkan kelengkapan kandungan gizi yang dibutuhkan.
</div>''',unsafe_allow_html=True)
    

with tab[1]:
    st.title("Latihan")
    nama = st.text_input("Nama",key="Nama")
    kelas = st.text_input("kelas",key="kelas")
    sekolah = st.text_input("sekolah",key="sekolah")
