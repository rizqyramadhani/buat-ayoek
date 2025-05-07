import tkinter as tk

# Variabel untuk menyimpan status apakah ucapan sudah ditampilkan
ucapan_tampil = False

def tampilkan_kue_dan_ucapan():
    global ucapan_tampil
    
    # ASCII Art untuk Kue Ulang Tahun
    cake = '''
           _..._  ,s$$$s.                                                                                          _..._  ,s$$$s.
         .$$$$$$$s$$ss$$$$,                                                                                     .$$$$$$$s$$ss$$$$,
         $$$sss$$$$s$$$$$$$                                                                                     $$$sss$$$$s$$$$$$$
         $$ss$$$$$$$$$$$$$$                                   (             )                                   $$ss$$$$$$$$$$$$$$
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                           '$$$s$$$$$$$$$$$$'
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                           '$$$$$$$$$$$$$$'
            S$$$$$$$$$$$'                             |      |~|           |~|      |                              S$$$$$$$$$$$'
             '$$$$$$$$$'                             |~|     | |           | |     |~|                              '$$$$$$$$$'
               '$$$$$'                               | |     | |           | |     | |                                '$$$$$'
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                '$$$'
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            ;
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         ; 
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . @@@@@@@@@@@@@@@@@@@@@@@@a                        ;
                 ',                         ;@@@@@@@@@@@@@@@@@@'   .   @@@@@@@@@@@@@@@@@@@@@';                        ',
                  ;                         ;@@@@@@@@@@@@@@@@'     .     @@@@@@@@@@@@@@@@'@@@;                         ;
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        ,'
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        ;
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        ',
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         ',
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          ;
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      '
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

    def tampilkan_ngeruning(teks, index=0):
        if index < len(teks):
            label_ucapan.config(text=teks[:index+1])
            root.after(100, tampilkan_ngeruning, teks, index+1)

    ucapan = (
        "selamat ulang tahun yaa sayangkuuuuuuuuuuuuuuuuuuuu, "
        "aku harap dengan  apapun doa atau keingin kamu bisa kamu dapetin . "
        "jangan pernah takut gagal yaa aku selalu support kamu sayagku,MAS RAMA SELALU NANG PINGGIRMU!!!!. "
        "semoga selalu di beri kelancaran dalam urusan dan kegiatan yang kamu lakuin. "
        "semangat koleyahnyaaa MOGA LANCAR TANPA HALANGAN ya doain aku juga yaaaaa hahahah. "
        "terimakasih ya apa yang kamu lakuin ke aku sangat tidak nyongko kamu sangat sangat tulus sama akauu."
        "maaf balum bisa jasi pasangan yang kamu harapin dan gaselalu ada di sampingmu karna  LDR YEEEE."
        "stay safe,stay healty, stay with mee eaaaaaaaaaa."
        "gatau deh ngomong apalagi. "
        "intinya happy birthday my love, my world, my universe."
        "segala doa yang baik adanya untukmu dan mimpimu yang mulia."
    )

    # Jika ucapan belum ditampilkan, tampilkan kue dan ucapan
    if not ucapan_tampil:
        # Menampilkan ASCII Art Kue
        label_kue.config(text=cake)
        label_ucapan.config(text="")  # Mengosongkan label sebelum memulai animasi
        tampilkan_ngeruning(ucapan)  # Menampilkan teks dengan efek ngeruning
        ucapan_tampil = True  # Mengubah status menjadi ucapan sudah ditampilkan
    else:
        # Menyembunyikan kue dan menampilkan ucapan lagi dengan efek ngeruning
        label_kue.config(text="")  # Menyembunyikan kue
        label_ucapan.config(text="")  # Mengosongkan label ucapan
        tampilkan_ngeruning(ucapan)  # Menampilkan teks dengan efek ngeruning
        ucapan_tampil = False  # Mengubah status menjadi ucapan belum ditampilkan

# Buat window utama
root = tk.Tk()
root.title("Ucapan Ulang Tahun")
root.geometry("800x800")  # Ukuran jendela diperbesar agar cukup untuk teks

# Tombol untuk menampilkan kue dan ucapan
tombol = tk.Button(root, text="pencet ya ndorooo", command=tampilkan_kue_dan_ucapan, font=("Arial", 14))
tombol.pack(pady=20)

# Label untuk ASCII art kue ulang tahun
label_kue = tk.Label(root, font=("Courier", 10), padx=10, pady=10, justify="center")
label_kue.pack()

# Label untuk ucapan panjang
label_ucapan = tk.Label(root, text="", wraplength=700, justify="center", font=("Arial", 12))
label_ucapan.pack(pady=20)

root.mainloop()
