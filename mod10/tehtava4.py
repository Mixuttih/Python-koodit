import random

#Kilpailuluokka
class Kilpailu:
    def __init__(self, nimi, pituus, lista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = lista

    def tunti_kuluu(self):
        #Käydään läpi jokainen auto
        for each in self.autolista:
            #Kiihdytetään -10 ja +15 väliltä satunnaisesti
            each.kiihdyta(random.randint(-10, 15))
            # Kuljetaan tunti
            each.kulje(1)

        #Nostetaan kuluneiden tuntien arvoa
        return kuluneet_tunnit+1

    def kilpailu_ohi(self):
        #Käydään läpi jokainen auto
        for each in self.autolista:
            #Jos joku auto on päässyt maaliin, lopetetaan kisa
            if each.kuljettumatka >= self.pituus:
                return True
        #Muutoin jatketaan kisaa
        return False

    def tulosta_tilanne(self):
        # "Selkeä taulukko"
        print('-' * 54)
        print('| {:^50} |'.format(kilpailu.nimi))
        print('-' * 54)
        print('| {:<13} | {:>15} | {:>16} |'.format('Auto', 'Huippunopeus', "Kuljettu matka"))
        print('-' * 54)
        for each in self.autolista:
            print('| {:<13} | {:>10} km/h | {:>13} km |'.format(each.rekisteritunnus, each.huippunopeus,
                                                                each.kuljettumatka))
        print('-' * 54)

#Autoluokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        #Tarkistetaan onko nopeuden muutos positiivinen
        if nopeudenmuutos > 0:
            #Tarkistetaan onko muutos alle huippunopeuden
            if nopeudenmuutos + self.nopeus <= self.huippunopeus:
                #Lisätään muutos nopeuteen
                self.nopeus += nopeudenmuutos
            #Tarkistetaan onko muutos yli huippunopeuden
            elif nopeudenmuutos + self.nopeus > self.huippunopeus:
                #Asetetaan nopeudeksi huippunopeus
                self.nopeus = self.huippunopeus

        #Jos muutos on negatiivinen
        else:
            #Tarkistetaan meneekö nopeuden muutos negatiiviseksi
            if nopeudenmuutos + self.nopeus < 0:
                #Asetetaan nopeus nollaan
                self.nopeus = 0
            #Jos nopeus on yhä positiivinen
            else:
                #Vähennetään muutos nopeudesta
                self.nopeus + nopeudenmuutos

    def kulje(self, tuntimaara):
        self.kuljettumatka += self.nopeus * tuntimaara

#Luodaan listamuuttuja
autolista = list()

#Parametrit autolistan generointiin
automaara = 10
autonumero = 1

#Seurataan kuluneita tunteja, jotta tiedetään milloin kutsua tilanteen tulostusta
kuluneet_tunnit = 0

#Loop joka lisää autoja listaan
while autonumero <= automaara:
    autolista.append(Auto(f"ABC-{autonumero}", random.randint(100,200)))
    autonumero += 1

#Kilpailun alustaminen
kilpailu = Kilpailu("Suuri Romuralli", 8000, autolista)

#Loop joka pyörii kunnes kilpailu on ohi
while kilpailu.kilpailu_ohi() == False:
    #Ajetaan tunti
    kuluneet_tunnit = kilpailu.tunti_kuluu()

    #Jos 10 tuntia kulunut, tulostetaan tulostaulu
    if kuluneet_tunnit % 10 == 0:
        print(f"Kuluneet tunnit: {kuluneet_tunnit}h")
        kilpailu.tulosta_tilanne()

#Kun kilpailu on ohi
if kilpailu.kilpailu_ohi() == True:
    print(f"Kilpailun pituus tunteina: {kuluneet_tunnit}h.")
    print("Lopullinen tilanne:")
    kilpailu.tulosta_tilanne()

    #Etsitään voittajan rekisteritunnus
    for each in kilpailu.autolista:
        if each.kuljettumatka > kilpailu.pituus:
            print(f"Voittaja on {each.rekisteritunnus}!")


