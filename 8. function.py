# perintah buatan sendiri/kumpulan perintah agar bisa digunakan berulang kali

def sapa(nama):
    print(f"Halo, {nama}!") #function paramenter

def datadiri(nama,alamat,umur):
    print(f"nama saya {nama}, alamat saya di {alamat}, umur saya {umur} tahun")

datadiri("Afifah","tungkop",18)



sapa("Afifah")
sapa("Nazira")

def sapa () :
    print("halo!")
    print("apa kabar?") #function tanpa parameter

    sapa()
    sapa()


# function dengan return = mengirim hasil kembali ke pemanggilnya,beda dgn print yg hanya menampilkan hasilnya saja
def luas_persegi(sisi):
    return sisi * sisi

# memanggil function dan menyimpan hasilnya
hasil = luas_persegi(5)
print(f"luasnya {hasil}")
print(f"luasnya {luas_persegi(3)}") #langsung memanggil function tanpa menyimpan hasilnya
