#menghitung luas segitiga dengan banyak jumlah sekaligus
jmlSegitiga = float(input("Masukan Jumlah segitiga yang ingin dihitung : "))
alas = float(input("Masukan Alas segitiga : "))
tinggi = float(input("Masukan Tinggi segitiga : "))
rumus = alas * tinggi/2
hasil = rumus * jmlSegitiga

print("Luas segitiga dengan alas %0.1f dan tinggi %0.1f ialah : %0.1f"%(alas, tinggi, hasil))