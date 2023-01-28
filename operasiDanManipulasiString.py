#operasi dan manipulasi string

#1. menyambung string (concatenate)
nama_pertama = "joni"
nama_tengah = "santoso"
nama_belakang = "sukirman"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

#2. menghitung panjang string (length)
panjang = len(nama_lengkap)
print("panjang dari", nama_lengkap, "adalah", panjang)

#operator untuk string

#1. mengecek keanggotaan (in)
d = "s"
status = d in nama_lengkap
print(d, "adalah anggota dari", nama_lengkap, ":", status)

d = "z"
status = d in nama_lengkap
print(d, "adalah anggota dari", nama_lengkap, ":", status)

#2. tidak keanggotaan (not in)
d = "s"
status = d not in nama_lengkap
print(d, "bukan anggota dari", nama_lengkap, ":", status)

d = "z"
status = d not in nama_lengkap
print(d, "bukan anggota dari", nama_lengkap, ":", status)

#3. operator untuk string
a = "halo"
b = "halo"

#pengecekan kesamaan
hasil = a is b
print(a, "is", b, ":", hasil)

#pengecekan tidak kesamaan
hasil = a is not b
print(a, "is not", b, ":", hasil)

#indexing
print("index ke 0 :", nama_lengkap[0])
print("index ke 1 :", nama_lengkap[1])
print("index ke-1 :", nama_lengkap[-1])
print("index ke-2 :", nama_lengkap[-2])
print("index ke 0-4 :", nama_lengkap[0:4])
print("index ke 0-4 :", nama_lengkap[:4])
print("index ke 5-akhir :", nama_lengkap[5:])
print("index ke -5-akhir :", nama_lengkap[-5:])
print("index ke 0-1-2-3-4 :", nama_lengkap[0:5:2])

#item paling kecil
print("paling kecil :", min(nama_lengkap))

#item paling besar
print("paling besar :", max(nama_lengkap))

ascii_code = ord("a")
print("ASCII code untuk karakter a adalah", ascii_code)

data = 115
print("karakter dari ASCII code 115 adalah", chr(data))

#4. operator dalam bentuk method
data = "halo dunia"
jumlah = data.count("a")
print("jumlah a pada", data, "adalah", jumlah)