#1
import random
luku = 0

def heittaja():
    arvo = random.randint(1, 6)
    return arvo

while luku != 6:
    luku = heittaja()
    print(luku)

#2
nopan_sivut = int(input("Monta kantaa nopassa on: "))
luku = 0

def heittaja2(sivut):
    arvo = random.randint(1, sivut)
    return arvo

while luku != nopan_sivut:
    luku = heittaja2(nopan_sivut)
    print(luku)

#3
gallonat = input("Kuinka monta gallonaa bensiiniä: ")
if gallonat == "":
    gallonat = 0

def gallonat_litroiksi(gal):
    litrat = gal * 3.785
    return litrat

while int(gallonat) >= 0:
    gallonat = gallonat_litroiksi(int(gallonat))
    print(f"Syötetty määrä on {gallonat} litraa")
    gallonat = input("Kuinka monta gallonaa bensiiniä: ")
    if gallonat == "":
        gallonat = 0

#4
luku_lista = []
luku_maara = 5

def listasumma(lista):
    summa = 0
    for n in lista:
        summa += n

    return summa

while luku_maara > 0:
    luku_lista.append(int(input("Syötä luku: ")))
    luku_maara -= 1

summa = listasumma(luku_lista)
print(f"Lukujen yhteenlaskettu summa on {summa}")

#5
luku_lista2 = []
luku_maara2 = 5
karsittava_lista = []

def listaparillinen(lista):
    for n in lista:
        if n % 2 != 0:
            karsittava_lista.remove(n)

while luku_maara2 > 0:
    numero = int(input("Syötä luku: "))
    luku_lista2.append(numero)
    karsittava_lista.append(numero)
    luku_maara2 -= 1

listaparillinen(karsittava_lista)

print(f"Alkuperäinen lukulista on {luku_lista2}")
print(f"Lukulista ilman parittomia lukuja on {karsittava_lista}")

#6
import math

pizza1_halkaisija = input("Kuinka suuri ensimmäisen pizzan halkaisija on senttimetreissä: ")
pizza1_hinta = input("Kuinka kallis ensimmäinen pizza on: ")
pizza2_halkaisija = input("Kuinka suuri toisen pizzan halkaisija on senttimetreissä: ")
pizza2_hinta = input("Kuinka kallis toinen pizza on: ")

def pizzalaskuri(halk1, halk2, hint1, hint2):
    pizza1_sade = halk1 / 2
    pizza2_sade = halk2 / 2
    pizza1_pinta_ala = math.pi * pizza1_sade**2
    pizza2_pinta_ala = math.pi * pizza2_sade**2
    pizza1_arvo = pizza1_pinta_ala / hint1
    pizza2_arvo = pizza2_pinta_ala / hint2
    print(f"Ensimmäisessä pizzassa maksat {pizza1_arvo:.2f} euroa per neliömetri")
    print(f"Toisessa pizzassa maksat {pizza2_arvo:.2f} euroa per neliömetri")

pizzalaskuri(int(pizza1_halkaisija), int(pizza2_halkaisija), int(pizza1_hinta), int(pizza2_hinta))
