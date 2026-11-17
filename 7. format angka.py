# format angka berfungsi untuk merapikan angka

# 2f untuk mengatur berapa koma yang mau diambil, misal 2f maka akan mengambil 2 angka dibelakang koma
angka = 3.14159
print(f"{angka:.2f}") 
#  6 untuk menandai lebar karakter ada 6
pi = 3.1415999777
print(f'*({pi:6.2f})*') #hasilnya akan ada 6 karakter, jika kurang maka akan diisi spasi
print(f'{pi:.4f}') #hasilnya akan ada 4 angka dibelakang koma

nama = 'afifah' 
namateman = 'nazira'



print(f'nama saya = {nama}')
print(f'{'nama saya':>9} = {nama}')

# contoh : daftar harga yg rapi
nasi = 12500.5
teh = 3000
print(f'nasi  {nasi:>10.2f}')
print(f'teh   {teh:>10.2f}')