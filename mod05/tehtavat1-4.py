#1

import random
noppien_maara = int(input("Kuinka monta noppaa heitetään: "))
summa = 0

for _ in range(noppien_maara):
    noppaluku = random.randint(1,6)
    print(f"Heitetyn nopan arvo on: {noppaluku}")
    summa = summa + noppaluku

print(f"Kaikkien heitettyjen noppien silmälukujen summa on: {summa}")

#2
syotetty_luku = input("Syötä luku: ")
luku_lista = []

while syotetty_luku != "":
    syotetty_luku = int(syotetty_luku)
    luku_lista.append(syotetty_luku)
    syotetty_luku = input("Syötä luku: ")

luku_lista.sort(reverse=True)
print(f"Viisi suurinta syötettyä lukua: {luku_lista[0:5]}")

#3
alkuluku_syote = int(input("Syötä luku: "))

onko_alkuluku = True

for i in range(2, alkuluku_syote):
    if alkuluku_syote % i == 0 :
        onko_alkuluku = False
        break

if onko_alkuluku:
   print("Syötetty luku on alkuluku")
else:
   print("Syötetty luku ei ole alkuluku")

#4
kaupunki_lista = []

for _ in range(1,6):
    kaupunki_lista.append(input("Kaupunki: "))

for kaupunki in kaupunki_lista:
    print(kaupunki)