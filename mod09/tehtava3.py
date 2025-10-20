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

#Alustetaan auto
auto1 = Auto("ABC-123", 142)

#Kiihdytetään 60km/h nopeuteen
auto1.kiihdyta(60)

#Kuljetaan 1,5h
auto1.kulje(1.5)
print(f"Kuljettu matka: {auto1.kuljettumatka} km")