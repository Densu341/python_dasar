#operator dalam bentuk method

# merubah case dari string

# merubah semua huruf menjadi huruf besar

salam = "halo dunia"
print(salam.upper())

# merubah semua huruf menjadi huruf kecil

salam = "HALO DUNIA"
print(salam.lower())

## pengecekan dengan isX method

# contoh pengecekan lower case dan upper case

salam = "halo dunia"
print(salam.islower())
print(salam.isupper())

# isaaplha() method <- mengecek apakah string berisi huruf saja
# isalnum() method <- mengecek apakah string berisi huruf dan angka saja
# isdecimal() method <- mengecek apakah string berisi angka saja
# isspace() method <- mengecek apakah string berisi spasi saja
# istitle() method <- mengecek apakah string berisi huruf kapital di awal kata saja

# istitle() method
judul = "Halo Dunia" # string berisi huruf kapital di awal kata
cek_judul = judul.istitle() # mengembalikan nilai boolean
print("Judul Apakah dia istitle ? "+str(cek_judul))

# ngecek komponen string dengan startswith() dan endswith() method

# startswith() method <- mengecek apakah string diawali dengan komponen tertentu
# endswith() method <- mengecek apakah string diakhiri dengan komponen tertentu
cek_start = "Saya Sedang Belajar Python".startswith("Saya") #case sensitive
print("start = "+ str(cek_start))

cek_end = "Saya Sedang Belajar Python".endswith("Python")
print("end = "+ str(cek_end))

# penggabungan komponen join() dan split() method
pisah = ['aku','sedang','belajar','python']
gabung = ' '.join(pisah) # menggabungkan komponen dengan spasi
print(pisah)
print(gabung)

gabungan = 'aku,sedang,belajar,python'
pisah = gabungan.split(',') # memisahkan komponen dengan koma
print(gabungan)

# alokasi karakter
print(5*'=' + ' halo ' + 5*'=') # mengalokasikan 5 karakter '=' di depan dan belakang string

# alokasi karakter dengan rjust() dan ljust() method
kanan = 'halo'.rjust(10) # mengalokasikan 10 karakter spasi di sebelah kanan string
print("'"+kanan+"'")

kiri = 'halo'.ljust(10) # mengalokasikan 10 karakter spasi di sebelah kiri string
print("'"+kiri+"'")

tengah = 'halo'.center(20,"=") # mengalokasikan 10 karakter spasi di sebelah kiri dan kanan string
print("'"+tengah+"'")

#kebalikan dari alokasi karakter dengan strip() method
tebgah = tengah.strip("=") # menghilangkan karakter '=' di sebelah kiri dan kanan string
print("'"+tebgah+"'")

kanan = kanan.strip() # menghilangkan karakter spasi di sebelah kanan string'
print("'"+kanan+"'")

kiri = kiri.strip() # menghilangkan karakter spasi di sebelah kiri string
print("'"+kiri+"'")
