# method string adalah function-function yang bisa digunakan untuk data dengan jenis string
# perintah bawaan untuk mengolak teks

# upper() = untuk mengubah semua huruf menjadi huruf besar
text = "hello world"
print(text.upper())

# lower() = untuk mengubah semua huruf menjadi huruf kecil
text = "HELLO WORLD"
print(text.lower())

# title() = untuk mengubah huruf pertama menjadi huruf besar
text = "hello world"    
print(text.title())   

# capitalize() = untuk mengubah huruf pertama menjadi huruf besar 
text = "hello world"
print(text.capitalize())

# strip() = untuk menghapus spasi di awal dan akhir string
kata = "          hello world        "
print(f'[{kata}]') 
print(f'[{kata.strip()}]') 

kata_2 ="          !!!!!!!!!!!!!###%%%%af!fa#####!!!!!!!"
print(f'[{kata_2}]')
print(f'[{kata_2.strip("!#% ")}]')

# l strip untuk menghapus karakter sebelah kiri string
kata_3 = "          hello world        "
print(f'[{kata_3}]')
print(f'[{kata_3.lstrip()}]')

kata_4 = "        af!fa           "
print(f'[{kata_4}]')
print(f'[{kata_4.rstrip()}]')

#find() = untuk mencari karakter tertentu di dalam string, jika tidak ditemukan maka akan mengembalikan nilai -1
text = "hello world"
print(text.find("o"))  # Output: 4
print(text.find("z"))  # Output: -1

# count() = untuk menghitung jumlah karakter tertentu di dalam string
nama = 'afifah'
print(nama.count('a'))  # Output: 3


