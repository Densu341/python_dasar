#cara membuat string

data = "ini adalah string"
print(data)
print(type(data))

'''
    1. dengan menggunakan tanda petik satu (')
    2. dengan menggunakan tanda petik dua (")

'''

data = 'menggunakan tanda petik satu'
print(data)

data = "menggunakan tanda petik dua"
print(data)

print('"mari belajar \"python\". yuk!"')

#backslash
print("C:\\user\\namauser")

#tab
print("nama\t: joni")

#backspace
print("nama : joni\bjoni")

#newline
print("baris pertama \nbaris kedua") #LF (line feed) -> unix, macos, linux
print("baris pertama \rbaris kedua") #CR (carriage return) -> commodore, acorn, lisp
print("baris pertama \r\nbaris kedua") #CRLF (carriage return & line feed) -> microsft, dos, inux, macos

#string literal atau raw
#hati-hati
# print('C:\new folder') #akan error
print(r'C:\new folder')

#multiline literal string
print("""
Nama : joni
kelas : 3 SD
""")

#multiline string literal dan raw
print(r"""
Nama : joni
kelas : 3 SD
website : www.joni.com/newID
""")