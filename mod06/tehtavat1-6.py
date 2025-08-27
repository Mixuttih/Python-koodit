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

def pizzalaskuri(halk, hint):
    pizza_sade = halk / 2
    pizza_pinta_ala = math.pi * pizza_sade**2
    pizza_arvo = hint / pizza_pinta_ala
    return pizza_arvo

pizza1_halkaisija = input("Kuinka suuri ensimmäisen pizzan halkaisija on senttimetreissä: ")
pizza1_hinta = input("Kuinka kallis ensimmäinen pizza on: ")

pizza1_arvo = pizzalaskuri(int(pizza1_halkaisija), int(pizza1_hinta))

pizza2_halkaisija = input("Kuinka suuri toisen pizzan halkaisija on senttimetreissä: ")
pizza2_hinta = input("Kuinka kallis toinen pizza on: ")

pizza2_arvo = pizzalaskuri(int(pizza2_halkaisija), int(pizza2_hinta))

print(f"Ensimmäisessä pizzassa maksat {pizza1_arvo:.2f} euroa per neliömetri")
print(f"Toisessa pizzassa maksat {pizza2_arvo:.2f} euroa per neliömetri")
if pizza1_arvo > pizza2_arvo:
    print(f"Pizza 2 on {pizza1_arvo - pizza2_arvo:.2f} euroa halvempi kuin Pizza 1")
elif pizza2_arvo > pizza1_arvo:
    print(f"Pizza 1 on {pizza2_arvo - pizza1_arvo:.2f} euroa halvempi kuin Pizza 2")
else:
    print("Pizzat ovat saman arvoisia, kaikki ovat tyytyväisiä")