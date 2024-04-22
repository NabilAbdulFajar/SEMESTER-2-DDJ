def berangkat_sekolah(pakaian, buku):
    if pakaian == "seragam" and buku == "bawa":
        print("berangkat sekolah")
    else:
        print("pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("kukima"), berangkat_sekolah("seragam", "bawa"))
print(nama_siswa("kuku"), berangkat_sekolah("jeans","tidak bawa buku "))
print(nama_siswa("keke"), berangkat_sekolah("seragam","tidak bawa buku"))




