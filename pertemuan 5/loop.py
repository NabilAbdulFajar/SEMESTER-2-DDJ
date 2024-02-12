



print("\nLOOPING IN PYTHON")
print("--------------------")
a = 0
b = float (input("masukan angka anda : " ))
while a < b: # a < b adalah  syarat .0 
    print(a)
    a += 1 # increment

print("\nPenggunaan Break pada Looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a) 
    if a == 15 : # Seleksi kondisi
        break # Break Point
    a += 1 # increment

print("\nPenggunaan Continue pada Looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # increment
    if a == 5: # Seleksi kondisi
        continue # Continue Point
    print(a)

print("\nPenggunaan if else pada Looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # increment
    if a == (b - 1): # Seleksi kondisi
        print ("perulangan berhenti")
        break;
    else:
        print("Perulangan ke -", a)
        a+= 1





















