import streamlit as st

# Variabel untuk menyimpan status apakah ucapan sudah ditampilkan
ucapan_tampil = False

def tampilkan_kue_dan_ucapan():
    global ucapan_tampil
    
    # ASCII Art untuk Kue Ulang Tahun
    cake = '''
           _..._  ,s$$$s.                                                                                          
         .$$$$$$$s$$ss$$$$,                                                                                     
         $$$sss$$$$s$$$$$$$                                                                                     
         $$ss$$$$$$$$$$$$$$                                   (             )                                   
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                          
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                          
            S$$$$$$$$$$$'                             |      |~|           |~|      |                             
             '$$$$$$$$$'                             |~|     | |           | |     |~|                             
               '$$$$$'                               | |     | |           | |     | |                                
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . @@@@@@@@@@@@@@@@@@@@@@@@a                        
                 ',                         ;@@@@@@@@@@@@@@@@@@'   .   @@@@@@@@@@@@@@@@@@@@@';                        
                  ;                         ;@@@@@@@@@@@@@@@@'     .     @@@@@@@@@@@@@@@@'@@@;                         
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      
                                     .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                    %%%%%%%%;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                    %%%%%%%%%%%%;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                    %%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                 """""""""""""",,,,,,,,,'"""""""""""""""""
                                                                %%%%%%%'
                                                                 %%%%%'
                                                                   %%% 
                                                                  %%%%%
                                                               .,%%%%%%%,.
                                                          ,%%%%%%%%%%%%%%%%%%%,
'''

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
    
    # Efek animasi ngeruning
    def tampilkan_ngeruning(teks, index=0):
        if index < len(teks):
            st.text(teks[:index+1])
            st.experimental_rerun()  # Mengulang halaman setiap beberapa detik
            st.time.sleep(0.1)
            tampilkan_ngeruning(teks, index+1)

    ucapan = (
        "selamat ulang tahun yaa sayangkuuuuuuuuuuuuuuuuuuuu, "
        "aku harap dengan apapun doa atau keingin kamu bisa kamu dapetin. "
        "jangan pernah takut gagal yaa aku selalu support kamu sayangku, MAS RAMA SELALU NANG PINGGIRMU!!!!. "
        "semoga selalu di beri kelancaran dalam urusan dan kegiatan yang kamu lakuin. "
        "semangat koleyahnyaaa MOGA LANCAR TANPA HALANGAN ya doain aku juga yaaaaa hahahah. "
        "terimakasih ya apa yang kamu lakuin ke aku sangat tidak nyongko kamu sangat sangat tulus sama akauu."
        "maaf balum bisa jadi pasangan yang kamu harapin dan gaselalu ada di sampingmu karna LDR YEEEE."
        "stay safe, stay healthy, stay with me eaaaaaaaaaa."
        "gatau deh ngomong apalagi. "
        "intinya happy birthday my love, my world, my universe."
        "segala doa yang baik adanya untukmu dan mimpimu yang mulia."
    )

    # Menampilkan kue dan ucapan
    if not ucapan_tampil:
        st.text(cake)
        tampilkan_ngeruning(ucapan)  # Menampilkan teks dengan efek ngeruning
        ucapan_tampil = True
    else:
        st.text("")  # Menyembunyikan kue
        tampilkan_ngeruning(ucapan)  # Menampilkan ucapan ulang tahun lagi dengan efek ngeruning
        ucapan_tampil = False

# Tombol untuk menampilkan kue dan ucapan
if st.button("pencet ya ndorooo"):
    tampilkan_kue_dan_ucapan()
