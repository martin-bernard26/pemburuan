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
    if nama and kelas and sekolah:
        st.markdown('''
                <div><b>Petunjuk</b>
                <ol type="a">
                    <li>Selesaikan tugas menyenangkan berikut!</li>
                    <li>Tulis jawaban dengan benar dan jelas!</li>
                    <li>Soal-soal berikut berdasarkan teks bacaan yang berjudul “Hemat Air, Cara Mudah Menyelamatkan Bumi”.</li>
                </ol>
                </div>
                ''', unsafe_allow_html=True)
        tulisan_html3=f'''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .pertanyaan{{
            font-family:"comic sans ms";
            font-size:20px;
            margin:10px;
            color:blue;
        }}
        .pertanyaan1, .pertanyaan2{{
            font-size:18px;
            color:black;
            font-weight:bold;
            margin:5px;
        }}
        .pertanyaan3{{
            border:2px solid brown;
            width:300px;
            height:30px;
            background-color:white;
            border-radius:10px;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan3:hover{{
            background-color:yellow;
            border-radius:5px;
        }}
        .pertanyaan4, .pertanyaan5{{
            border-radius:10px;
            border:2px solid black;
            box-shadow:2px 2px 2px 2px green;
            background-color:white;
            font-size:15px;
            padding:3px;
        }}
        .pertanyaan4:hover, .pertanyaan5:hover{{
            background-color:cyan;
        }}
        .pertanyaan4:focus, .pertanyaan5:focus{{
            background-color:lightgoldenrodyellow;
            font-size:15px;
            padding:3px;
        }}
        #kirim1{{
            font-family:nroadway;
            font-size:20px;
            background-color:green;
            color:yellow;
        }}
    </style>
</head>
<body>
    <div>
        <div><input type="text" id="nama" value={nama}></div>
        <div><input type="text" id="kelas" value={kelas}></div>
        <div><input type="text" id="ns" value={sekolah}></div>
    </div>
    <div>
        <ol>
            <li class="pertanyaan"><b>Artikan kata-kata/kelompok kata berikutnya</b>
                <ol type="a">
                    <li class="pertanyaan1">Konsumsi  (baris ke-6)  =  <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Rekomendasi (baris ke-10)  = <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Idealnya (baris ke-11) =  <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Membentengi diri (baris ke-12)  =   <input class="pertanyaan3" type="text"> </li>
                    <li class="pertanyaan1">Merekomendasikan (baris ke-25)  = <input class="pertanyaan3" type="text"></li>
                </ol>
            </li>
            <li class="pertanyaan"><b>Jawablah pertenyaan di bahwah ini</b>
                <ol type="a">
                    <li class="pertanyaan2"><div>Apa nama masakan yang mengandung sayur, yang ada dalam teks bacaan tadi?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa saja zat penting yang terkandung dalam sayur dan buah?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                     </li>
                    <li class="pertanyaan2"><div>Apa yang dibahas dalam teks bacaan tadi?</div>
                        <div><textarea class="pertanyaan5" cols="40" rows="5"></textarea></div>
                    </li>
                </ol>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan informasi-informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan informasi-informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Uraikan ide pokok dan ide penjelas dalam teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Urutkan kejadian-kejadian dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tentukan kalimat utama dalam teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Urutkan fakta-fakta/informasi penting dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Tuliskan simpulan yang mengakibatkan masyarakat Indonesia kurang
                mengonsumsi sayur dan buah!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Ceritakan kembali dengan bahasamu sendiri isi teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Isi dalam teks bacaan tadi banyak mengandung makna/nilai-nilai/kebiasaan yang bisa kita tiru. 
                Tuliskan kebiasaan/nilai-nilai yang kamu pahami dari teks bacaan tadi!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah teks bacaan tadi jelas dan lengkap? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, alur tulisan yang dituliskan penulis sudah benar? Apa alasanmu?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Berdasarkan cerita dalam teks tadi, apakah ada informasi, data, atau fakta yang kamu temui
                dalam kehidupan sehari-hari? Jika ada, coba tuliskan!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>Menurutmu, apakah isi cerita dalam teks tadi sesuai dengan kehidupan sehari-hari? Mengapa?</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
            <li class="pertanyaan">
                <b>M16.	Setelah membaca cerita tadi, apakah ada nilai/kebiasaan yang perlu ditiru dan tidak boleh ditiru
                olehmu? Tuliskan nilai-nilai/kebiasaan yang perlu ditiru dan tidak perlu ditiru olehmu, yang akan kamu
                terapkan dalam kehidupan sehari-hari!</b>
                <div><textarea class="pertanyaan4" cols="40" rows="10"></textarea></div>
            </li>
        </ol>
    </div>
    <div><input id="kirim1" type="button" value="Kirim Jawaban" ></div>
    <script type="module">
            // Konfigurasi Firebase SDK
            import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
            const firebaseConfig = {{
                    apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                    authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                    databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                    projectId: "natural-ethos-423713-e0",
                    storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                    messagingSenderId: "41833960811",
                    appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
            }};

            // Inisialisasi Firebase
            const app = initializeApp(firebaseConfig);
            import {{getDatabase, set, get, update, remove, ref, child}}
                from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
            const db=getDatabase()
            var kirim1 = document.getElementById("kirim1")
            kirim1.addEventListener("click",()=>{{
                var nama = document.getElementById("nama").value
                var kelas = document.getElementById("kelas").value
                var ns = document.getElementById("ns").value
                var soal1 = document.getElementsByClassName("pertanyaan3")
                var soal2 = document.getElementsByClassName("pertanyaan5")
                var soal3 = document.getElementsByClassName("pertanyaan4")
                set(ref(db, 'pemburuan_hewan/' + nama), {{ 
                    nama:nama,
                    kelas:kelas,
                    ns:ns,
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
                set(ref(db, 'sayuran/' + nama+'/soal'), {{ 
                    soal1a:soal1[0].value,
                    soal1b:soal1[1].value,
                    soal1c:soal1[2].value,
                    soal1d:soal1[3].value,
                    soal1e:soal1[4].value,
                    soal2a:soal2[0].value,
                    soal2b:soal2[1].value,
                    soal2c:soal2[2].value,
                    soal3:soal3[0].value,
                    soal4:soal3[1].value,
                    soal5:soal3[2].value,
                    soal6:soal3[3].value,
                    soal7:soal3[4].value,
                    soal8:soal3[5].value,
                    soal9:soal3[6].value,
                    soal10:soal3[7].value,
                    soal11:soal3[8].value,
                    soal12:soal3[9].value,
                    soal13:soal3[10].value,
                    soal14:soal3[11].value,
                    soal15:soal3[12].value,
                    soal15:soal3[16].value
                }})
                    .then(() => {{
                        alert('Data added successfully');
                    }})
                    .catch((error) => {{
                    console.error("Error adding data:", error);
                }});
            }});

    </script>
</body>
</html>
'''
        st.components.v1.html(tulisan_html3,width=1000,height=13000)
