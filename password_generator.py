import random
import string

print("=== PASSWORD GENERATOR ===")
jumlah = int(input("Berapa password yang ingin dibuat?  "))
panjang = int(input("Panjang password:  "))

pakai_simbol = input("Pakai simbol? [y/n]:  ")

karakter = string.ascii_letters + string.digits

if pakai_simbol.lower() == "y":
    karakter += string.punctuation

print("\nPassword baru anda adalah: ")

for i in range(jumlah):
    password = ""
    for j in range(panjang):
        password += random.choice(karakter)
    print(f"{i+1}.  {password}" )
