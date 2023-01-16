# mengambil input dari user

#data pasti string
data = input("masukkan data : ")
print("data :", data, ", bertipe :", type(data))

#jika ingin mengambil int
angka = int(input("masukkan angka : "))
angka = float(input("masukkan angka : "))
print("data :", angka, ", bertipe :", type(angka))

#jika ingin mengambil boolean
biner = bool(int(input("masukkan nilai boolean : ")))
print("data :", biner, ", bertipe :", type(biner))