#1
i = 1

while i < 1000:
    if i % 3 == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1

#2

tuumat = float(input("Syötä tuumat: "))

while tuumat >= 0:
        sentit = tuumat * 2.54
        print("Syötetyt tuumat senttimetreinä: " + str(sentit) + "cm")
        tuumat = float(input("Syötä tuumat: "))


#3

luku = input("Syötä luku: ")
lukulista = []

while luku != "":
    luku = int(luku)
    lukulista.append(luku)
    luku = input("Syötä luku: ")

if len(lukulista) > 1:
    isoin_numero = max(lukulista)
    pienin_numero = min(lukulista)
    print("Suurin syötetty numero oli " + str(isoin_numero) + " ja pienin numero oli " + str(pienin_numero))
else:
    print("Lukuja ei syötetty tarpeeksi.")

#4
import random
arvattava_luku = random.randint(1, 10)

arvaus = int(input("Arvaa tietokoneen arpoma luku väliltä 1-10: "))

while arvaus != arvattava_luku:
    print("Väärin")
    if arvaus < arvattava_luku:
        print("Liian matala arvaus")
    if arvaus > arvattava_luku:
        print("Liian korkea arvaus")
    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein! Arvattava luku oli " + str(arvattava_luku))

#5
tunnus = input("Tunnus: ")
salasana = input("Salasana: ")

oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 5

while yritykset > 0:
    if tunnus == oikea_tunnus:
        if salasana == oikea_salasana:
            print("Tervetuloa")
            break

        else:
            yritykset = yritykset - 1
            if yritykset == 0:
                print("Liikaa vääriä yrityksiä, kirjautuminen estetty")
                break

            print("Pääsy evätty, yrityksiä jäljellä " + str(yritykset))

            tunnus = input("Tunnus: ")
            salasana = input("Salasana: ")
    else:
        yritykset = yritykset - 1
        if yritykset == 0:
            print("Liikaa vääriä yrityksiä, kirjautuminen estetty")
            break

        print("Pääsy evätty, yrityksiä jäljellä " + str(yritykset))

        tunnus = input("Tunnus: ")
        salasana = input("Salasana: ")


#6 käyttäen listaa ja for -looppia
syotteen_maara = int(input("Syötä pisteiden määrä: "))
pisteiden_maara = syotteen_maara
piste_lista = {}
ympyran_sisalla = 0
ympyran_ulkopuolella = 0


while pisteiden_maara > 0:
    piste_lista[pisteiden_maara] = random.uniform(-1, 1), random.uniform(-1, 1)
    pisteiden_maara = pisteiden_maara - 1

for piste in piste_lista:
    if piste_lista[piste][0]**2 + piste_lista[piste][1]**2 < 1:
        ympyran_sisalla = ympyran_sisalla + 1
    else:
        ympyran_ulkopuolella = ympyran_ulkopuolella + 1

print(f"Ympyrän sisällä on {ympyran_sisalla} pistettä")
print(f"Ympyrän ulkopuolella on {ympyran_ulkopuolella} pistettä")

pii_likiarvo = (ympyran_sisalla / syotteen_maara) * 4
print(f"Pii:n likiarvo on {pii_likiarvo}")

#6 uudelleen ilman listaa ja for -looppia
syotteen_maara2 = int(input("Syötä pisteiden määrä: "))
pisteiden_maara2 = syotteen_maara2
ympyran_sisalla2 = 0
ympyran_ulkopuolella2 = 0

while pisteiden_maara2 > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    pisteiden_maara2 = pisteiden_maara2 - 1

    if x**2 + y**2 < 1:
        ympyran_sisalla2 = ympyran_sisalla2 + 1
    else:
        ympyran_ulkopuolella2 = ympyran_ulkopuolella2 + 1

print(f"Ympyrän sisällä on {ympyran_sisalla2} pistettä")
print(f"Ympyrän ulkopuolella on {ympyran_ulkopuolella2} pistettä")
pii_likiarvo2 = (ympyran_sisalla2 / syotteen_maara2) * 4
print(f"Pii:n likiarvo on {pii_likiarvo2}")
