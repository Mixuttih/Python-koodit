import random

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

#Loop joka lisää autoja listaan
while autonumero <= automaara:
    autolista.append(Auto(f"ABC-{autonumero}", random.randint(100,200)))
    autonumero += 1

#Muuttuja joka lopettaa kisan
voittaja = ""

#Loop joka pyörii kunnes voittaja löytyy
while voittaja == "":
    #Käydään läpi jokainen auto
    for each in autolista:
        #Kiihdytetään autoa
        each.kiihdyta(random.randint(-10,15))
        #Kuljetaan tunti
        each.kulje(1)
        #Tarkistetaan onko auto ylittänyt maaliviivan
        if each.kuljettumatka > 10000:
            #Asetetaan voittaja
            voittaja = each.rekisteritunnus

print(f"Voittaja-auto on: {voittaja}!")

#"Selkeä taulukko"
print('-' * 36)
print('| {:<13} | {:<13} |'.format('Auto', 'Kuljettu matka'))
print('-' * 36)
for each in autolista:
    print('| {:<13} | {:>13} km |'.format(each.rekisteritunnus, each.kuljettumatka))
print('-' * 36)