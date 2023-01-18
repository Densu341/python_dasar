# episode latihan logika dan komparasi

#membuat gabungan area rentang dari angka

#++++++3--------10+++++++

from xml.etree.ElementTree import Comment


inputUser = float(input("masukan angka yang bernilai \n3 < angka > 10 : "))


#++++++3------------------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser) < 3

#=============10++++++++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser) > 10

#++++++3--------10+++++++
#memeriksa angka diantara 3 dan 10
isCorect = isKurangDari or isLebihDari
print("angka yang anda masukan adalah : ", isCorect)

#++++++3--------10+++++++
#kasus irisan
inputUser = float(input("masukan angka yang bernilai \n3 <  dan angka < 10 : "))

#======3+++++++++++++++
#memeriksa angka lebih dari 3
isLebihDari = (inputUser) > 3

#++++++++++++++10======
#memeriksa angka kurang dari 10
isKurangDari = (inputUser) < 10

#======3+++++++++++++++10======
#memeriksa angka diantara 3 dan 10
isCorect = isLebihDari and isKurangDari
print("angka yang anda masukan adalah : ", isCorect)

# nsvjbsbdscbd
# dsjcbsducbd
# cdcbdcdhcv