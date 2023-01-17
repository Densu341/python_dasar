#operasi logika atau boolean

#not, or, and, xor

from calendar import c


print("=====NOT=====")
a = True
c = not a

print("data a = ", a)
print("----------------NOT")
print("data c = ", c)

#jika salah satu true maka hasilnya true
print("=====OR=====")
a = True
b = False
c = a or b

print("data a = ", a)
print("data b = ", b)
print("----------------OR")
print("data c = ", c)

#jika keduanya true maka hasilnya true
print("=====AND=====")
a = True
b = False
c = a and b

print("data a = ", a)
print("data b = ", b)
print("----------------AND")
print("data c = ", c)

#jika keduanya beda maka hasilnya true
print("=====XOR=====")
a = True
b = False
c = a ^ b

print("data a = ", a)
print("data b = ", b)
print("----------------XOR")
print("data c = ", c)