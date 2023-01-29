# Kalkulator by densu

print(10*"=","Kalkulator By Densu","="*10)
angka1 = float(input("Masukkan angka pertama\t: "))
angka2 = float(input("Masukkan angka kedua\t: "))
print("Pilih operasi matematika")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilih = input("Masukkan pilihan (1/2/3/4)\t: ")
if pilih == '1':
    print(f"Hasil Dari {angka1} + {angka2} = ",angka1+angka2)
elif pilih == '2':
    print(f"Hasil Dari {angka1} - {angka2} = ",angka1-angka2)
elif pilih == '3':
    print(f"Hasil Dari {angka1} * {angka2} = ",angka1*angka2)
elif pilih == '4':
    print(f"Hasil Dari {angka1} / {angka2} = ",angka1/angka2)
else:
    print("Input salah")
print("Program selesai")