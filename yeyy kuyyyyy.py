iimport streamlit as st
import time

# Inisialisasi state
if 'tahap' not in st.session_state:
    st.session_state.tahap = 0  # 0: belum apa-apa, 1: tampil wish, 2: tampil ucapan

# Data
wish = ''' 
 /$$   /$$                                             /$$       /$$             /$$     /$$             /$$                                                      
| $$  | $$                                            | $$      |__/            | $$    | $$            | $$                                                      
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$    | $$$$$$$  /$$  /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$                                  
| $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$| $$  | $$    | $$__  $$| $$ /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$ |____  $$| $$  | $$                                  
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  | $$    | $$  \ $$| $$| $$  \__/  | $$    | $$  \ $$| $$  | $$  /$$$$$$$| $$  | $$                                  
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$    | $$  | $$| $$| $$        | $$ /$$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$                                  
| $$  | $$|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$$    | $$$$$$$/| $$| $$        |  $$$$/| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$                                  
|__/  |__/ \_______/| $$____/ | $$____/  \____  $$    |_______/ |__/|__/         \___/  |__/  |__/ \_______/ \_______/ \____  $$                                  
                    | $$      | $$       /$$  | $$                                                                     /$$  | $$                                  
                    | $$      | $$      |  $$$$$$/                                                                    |  $$$$$$/                                  
                    |__/      |__/       \______/                                                                      \______/                                   
'''

ucapan = (
    "selamat ulang tahun yaa sayangkuuuuuuuuuuuuuuuuuuuu, "
    "aku harap dengan apapun doa atau keingin kamu bisa kamu dapetin. "
    "jangan pernah takut gagal yaa aku selalu support kamu sayangku, MAS RAMA SELALU NANG PINGGIRMU!!!!. "
    "semoga selalu di beri kelancaran dalam urusan dan kegiatan yang kamu lakuin. "
    "semangat koleyahnyaaa MOGA LANCAR TANPA HALANGAN ya doain aku juga yaaaaa hahahah. "
    "terimakasih ya apa yang kamu lakuin ke aku sangat tidak nyongko kamu sangat sangat tulus sama akauu. "
    "maaf balum bisa jadi pasangan yang kamu harapin dan gaselalu ada di sampingmu karna LDR YEEEE. "
    "stay safe, stay healthy, stay with me eaaaaaaaaaa. "
    "gatau deh ngomong apalagi. "
    "intinya happy birthday my love, my world, my universe. "
    "segala doa yang baik adanya untukmu dan mimpimu yang mulia."
)

# Fungsi animasi teks berjalan
def tampilkan_ngeruning(teks):
    progress_text = st.empty()
    for i in range(1, len(teks) + 1):
        progress_text.markdown(f"<p style='text-align: center;'>{teks[:i]}</p>", unsafe_allow_html=True)
        time.sleep(0.07)

# Tombol dan aksi
if st.button("pencet ya ndorooo"):
    if st.session_state.tahap == 0:
        st.session_state.tahap = 1
    elif st.session_state.tahap == 1:
        st.session_state.tahap = 2

# Tampilan berdasarkan tahap
if st.session_state.tahap == 1:
    st.markdown(f"<pre style='text-align: center;'>{wish}</pre>", unsafe_allow_html=True)
elif st.session_state.tahap == 2:
    tampilkan_ngeruning(ucapan)
