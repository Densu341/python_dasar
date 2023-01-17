#operasi komparasi
#setiap hasil operasi komparasi adalah boolean

a = 5
b = 4


#> lebih besar dari /harus lebih besar dari
print("===== lebih besar dari =====")
hasil = a > b
print(a,'>',b,'=',hasil)

#< lebih kecil dari /harus lebih kecil dari
print("===== lebih kecil dari =====")
hasil = b < a
print(b,'<',a,'=',hasil)

#>= lebih besar dari sama dengan /boleh lebih besar dari atau sama dengan
print("===== lebih besar dari atau sama dengan =====")
hasil = a >= 5
print(a,'>=',5,'=',hasil)

#<= lebih kecil dari sama dengan /boleh lebih kecil dari atau sama dengan
print("===== lebih kecil dari atau sama dengan =====")
hasil = b <= a
print(b,'<=',a,'=',hasil)

#== sama dengan /harus sama dengan
print("===== sama dengan =====")
hasil = a == 5
print(a,'==',5,'=',hasil)
print(a,'==',b,'=',a==b)

#!= tidak sama dengan /harus tidak sama dengan
print("===== tidak sama dengan =====")
hasil = a != 5
print(a,'!=',5,'=',hasil)
print(a,'!=',b,'=',a!=b)
#operator diatas dapat bekerja pada sintax literal maupun variabel


#membandingkan memori / object
#is sama dengan / sebagai komparasi object identity
print("===== is sama dengan =====")
hasil = a is 5
print(a,'is',5,'=',hasil)
print(a,'is',b,'=',a is b)

#is not tidak sama dengan /harus tidak sama dengan
print("===== is not tidak sama dengan =====")
hasil = a is not 5
print(a,'is not',5,'=',hasil)
print(a,'is not',b,'=',a is not b)