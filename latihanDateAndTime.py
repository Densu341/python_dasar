# Date and Time(latihan)

import datetime as dt

#latihan prediksi hari lahir
print(5*"="+"Silahkan Masukan Tanggal Lahir Anda"+5*"=")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)

print("\n"+5*"="+"Hasil Prediksi"+5*"=")
print(f"Tanggal lahir\t {tanggal_lahir}")
print(f"Lahir Pada hari\t: {tanggal_lahir:%A, %B, %Y}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Hari ini adalah \t: {hari_ini:%A}")
print(f"Umur Anda adalah\t: {umur_hari.days} hari")
print(f"Umur Anda adalah\t: {umur_tahun} tahun")
print(f"Umur Anda adalah\t: {umur_bulan} bulan")



#coba-coba
# hari_ini = dt.date.today()
# print(f"Hari ini adalah hari: {hari_ini:%A, %B, %Y}")

# tanggal = dt.date(2002,4,10)
# print(f"Tanggal lahir saya adalah: {tanggal:%A, %B, %Y}")

