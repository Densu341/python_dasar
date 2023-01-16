#operasi aritmatika

a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

#operasi kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi kali *
hasil = a * b
print(a, "*", b, "=", hasil)

#operasi bagi /
hasil = a / b
print(a, "/", b, "=", hasil)

#operasi eksponen ** (pangkat)
hasil = a ** b
print(a, "**", b, "=", hasil)

#operasi modulus % (sisa bagi)
hasil = a % b
print(a, "%", b, "=", hasil)

#operasi floor division // (pembulatan ke bawah) /counter part dari modulus
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi ()
'''
    1. eksponen **
    2. perkalian, pembagian, modulus, floor division
    3. penjumlahan, pengurangan
'''

x = 3
y = 2
z = 4

hasil = x**y * (z + x) / y - y % z//x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = (x + y) * z
print(x, "+", y, "*", z, "=", hasil)