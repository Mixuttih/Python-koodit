#1
from ipaddress import summarize_address_range

kayttaja = input("Anna nimesi: ")
print("Terve, " + kayttaja + "!")

#2
ympyra = input("Määritä ympyrän säde cm: ")
sade = float(ympyra) * float(ympyra) * 3.14
print("Ympyrän pinta-ala on " + str(sade) + " cm2.")

#3
kulmio_sivu_a = input("Määritä suorakulmion ensimmäisen sivun pituus: ")
kulmio_sivu_b = input("Määritä suorakulmion toisen sivun pituus: ")

kulmio_pintaala = float(kulmio_sivu_a) * float(kulmio_sivu_b)
kulmio_piiri = float(kulmio_sivu_a) + float(kulmio_sivu_b) + float(kulmio_sivu_a) + float(kulmio_sivu_b)

print("Suorakulmion pinta-ala on " + str(kulmio_pintaala))
print("Suorakulmion piiri on " + str(kulmio_piiri))

#4
luku1 = input("Anna ensimmäinen kokonaisluku: ")
luku2 = input("Anna toinen kokonaisluku: ")
luku3 = input("Anna kolmas kokonaisluku: ")

summa = int(luku1) + int(luku2) + int(luku3)
tulo = int(luku1) * int(luku2) * int(luku3)
keskiarvo = (int(luku1) + int(luku2) + int(luku3)) / 2

print("Lukujen " + luku1 + ", " + luku2 + " ja " + luku3 + " summa on " + str(summa))
print("Lukujen " + luku1 + ", " + luku2 + " ja " + luku3 + " tulo on " + str(tulo))
print("Lukujen " + luku1 + ", " + luku2 + " ja " + luku3 + " keskiarvo on " + str(keskiarvo))

#5