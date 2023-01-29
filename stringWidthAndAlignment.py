#width and multiline

#data 
data_nama = "Deni"
data_umur = 20
data_tinggi = 170.5
data_nomor_sepatu = 40

#string standard
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)

#string Multiline (enter, new line)
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nNomor Sepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "Data String" + 5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""Nama            = {data_nama}
Umur            = {data_umur}
Tinggi          = {data_tinggi}
Nomor Sepatu    = {data_nomor_sepatu}
"""
print("\n"+5*"=" + "Data String" + 5*"=")
print(data_string)

#mengatur lebarnya
data_string = f"""Nama            = {data_nama:>5}
Umur            = {data_umur:>5}
Tinggi          = {data_tinggi:>5}
Nomor Sepatu    = {data_nomor_sepatu:>5}
"""
print("\n"+5*"=" + "Data String" + 5*"=")
print(data_string)