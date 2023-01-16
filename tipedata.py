#tipe data apa aja yang ada di python
#tipe data : angka satuan /integer
data_integer = 1
print("data :", data_integer)

print(type(data_integer))
print("data :", data_integer)
print("bertype :", type(data_integer))

#tipe data : angka dengan koma/float
data_float = 1.5
print("data :", data_float)
print("bertype :", type(data_float))

#tipe data : kumpulan karakter/ string
data__string = "ucup 10"
print("data :", data__string)
print("bertype :", type(data__string))

#tipe data : biner true/false (boolean)
data_boolean = True
print("data :", data_boolean)
print("bertype :", type(data_boolean))

#tipe data khusus
#bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("bertype :", type(data_complex))

#tipe data dari bahasa c

from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("bertype :", type(data_c_double))