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

autolista = list()

automaara = 10
autonumero = 1

while autonumero <= automaara:
    autolista.append(Auto(f"ABC-{autonumero}", random.randint(100,200)))
    autonumero += 1

voittaja = ""

while voittaja == "":
    for each in autolista:
        if each.kuljettumatka < 10000:
            each.kiihdyta(random.randint(-10,15))
            each.kulje(1)
            if each.kuljettumatka > 10000:
                voittaja = each.rekisteritunnus
                break
        else:
            voittaja = each.rekisteritunnus
            break

for each in autolista:
    print(f"Auto: {each.rekisteritunnus} - Huippunopeus: {each.huippunopeus} - Kuljettu matka: {each.kuljettumatka}")