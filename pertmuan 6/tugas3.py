belanja = [
    {"produk":"baju", "jumlah":20},
    {"produk":"celana", "jumlah":16},
    {"produk":"sepatu","jumlah":25},
    {"produk":"tas", "jumlah":10},
    ]
total_belanjaan = 0
for item in belanja:
    total_belanjaan += item ["jumlah"]

print("total belanja : ", total_belanjaan)

    