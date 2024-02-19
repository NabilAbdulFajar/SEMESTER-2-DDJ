belanja = [
    {"buah":"semangka", "harga":12000},
    {"buah":"pepaya", "harga":10000},
    {"buah":"nanas","harga":12000},
    ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item ["harga"]

print("total belanja : ", total_belanjaan)
