#latihan konversi satuan temperatur

#program konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR \n")

#input suhu dalam celcius
celcius = float(input("Masukkan suhu (Celcius): "))
print("Suhu adalah", celcius, "Celcius")

#reamur
#rumus: 4/5 * C
reamur = (4/5) * celcius
print("Suhu dalam Reamur:", reamur)

#fahrenheit
#rumus: 9/5 * C + 32
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit:", fahrenheit)

#kelvin
#rumus: C + 273
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

#konversi fahrenheit ke kelvin
#rumus: (F - 32) * 5/9 + 273
fahrenheit = float(input("Masukkan suhu (Fahrenheit): "))
print("Suhu adalah", fahrenheit, "Fahrenheit")

#konversi ke kelvin
kelvin = (fahrenheit - 32) * (5/9) + 273
print("Suhu dalam Kelvin:", kelvin)

#konversi kelvin ke fahrenheit
#rumus: (K - 273) * 9/5 + 32
kelvin = float(input("Masukkan suhu (Kelvin): "))
print("Suhu adalah", kelvin, "Kelvin")

#konversi ke fahrenheit
fahrenheit = (kelvin - 273) * (9/5) + 32
print("Suhu dalam Fahrenheit:", fahrenheit)