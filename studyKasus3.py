#program sederhana menghitung keramik yang diperlukan untuk lantai/ruangan
print("<==========PROGRAM HITUNG KERAMIK==========>")
ruang = int(input("Masukan jumlah ruangan yang ingin dipasang keramik : "))

pRuang = int(input("Masukan Panjang ruangan yang ingin dipasang keramik dalam CM : "))
lRuang = int(input("Masukan Lebar ruangan yang ingin dipasang keramik dalam CM : "))

pKeramik = int(input("Masukan Panjang keramik yang akan digunakan dalam CM : "))
lKeramik = int(input("Masukan Lebar keramik yang akan digunakan dalam CM : "))

#rumus
luasTotalRuang = (pRuang*lRuang)*ruang
luasKeramik = (pKeramik*lKeramik)
result = (luasTotalRuang/luasKeramik)

#output
print("Jumlah Keramik yang diperlukan untuk %i Ruangan ialah %0.2f Keramik dengan ukuran %i cm X %i cm"%(ruang, result, pKeramik, lKeramik))