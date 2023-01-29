#format string 

# contoh generic
# string
nama = 'Andi'
format_str = f"halo {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat {angka:d}"
print(format_str)

# bilangan bulat dengan 3 digit
angka = 2000000
format_str = f"ribuan {angka:,}"
print(format_str)

#bilangan desimal
angka = 2005.54321
format_str = f"desimal {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -2005.54321
format_str = f"minus {angka_minus:+.3f}"
print(format_str)

angka_plus = 2005.54321
format_str = f"plus {angka_plus:+.3f}"
print(format_str)

# memformat persen
persentase = 0.045
format_persen = f"persen {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 20000
jumlah = 5

format_str = f"total Rp.{harga*jumlah:,}"
print(format_str)

# contoh lain
#format angka lain (binary, octal, hexadecimal)
angka = 2005
format_str = f"binary {angka:b}"
print(format_str)

format_str = f"octal {angka:o}"
print(format_str)

format_str = f"hexadecimal {angka:x}"
print(format_str)