#belajar casting
#casting ialah merubah tipe data dari satu tipe ke tipe lain
#tipe data = int, float, str, bool

##integer
print("=======INTEGER=======")
data_int = 9
print("data :", data_int, ", bertipe :", type(data_int))

data_float = float(data_int)
print("data :", data_float, ", bertipe :", type(data_float))

data_str = str(data_int)
print("data :", data_str, ", bertipe :", type(data_str))

data_bool = bool(data_int) #akan bernilai false jika nilai 0
print("data :", data_bool, ", bertipe :", type(data_bool))

##float
print("=======FLOAT=======")
data_float = 9.5 
print("data :", data_float, ", bertipe :", type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
print("data :", data_int, ", bertipe :", type(data_int))

data_str = str(data_float)
print("data :", data_str, ", bertipe :", type(data_str))

data_bool = bool(data_float) #akan bernilai false jika nilai 0
print("data :", data_bool, ", bertipe :", type(data_bool))

##boolean
print("=======BOOLEAN=======")
data_boolean = True
print("data :", data_boolean, ", bertipe :", type(data_boolean))

data_int = int(data_boolean) #akan dibulatkan kebawah
print("data :", data_int, ", bertipe :", type(data_int))

data_str = str(data_boolean)
print("data :", data_str, ", bertipe :", type(data_str))

data_float = float(data_boolean) #akan bernilai false jika nilai 0
print("data :", data_float, ", bertipe :", type(data_float))

##string
print("=======STRING=======")
data_str = "10"
print("data :", data_str, ", bertipe :", type(data_str))

data_int = int(data_str) #string harus angka
print("data :", data_int, ", bertipe :", type(data_int))

data_bool = bool(data_str) #akan bernilai false jika string kosong
print("data :", data_bool, ", bertipe :", type(data_bool))

data_float = float(data_str) #string harus angka
print("data :", data_float, ", bertipe :", type(data_float))