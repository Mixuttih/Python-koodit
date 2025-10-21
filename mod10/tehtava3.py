class Hissi():
    def __init__(self):
        #Uusi hissi on kerroksessa 1
        self.kerros = 1

    def siirry_ylos(self, siirtyma, hissi):
        print(f"Alkupiste: Hissi {hissi} on kerroksessa {self.kerros}")
        #Noustaan kerroksia kunnes saavutetaan haluttu kerros
        while self.kerros < siirtyma and siirtyma <= talo.ylin_kerros:
            self.kerros += 1
            print(f"Hissi {hissi} meni kerrokseen {self.kerros}")
        print(f"Loppupiste: Hissi {hissi} on kerroksessa {self.kerros}")

    def siirry_alas(self, siirtyma, hissi):
        print(f"Alkupiste: Hissi {hissi} on kerroksessa {self.kerros}")
        #Lasketaan kerroksia kunnes saavutetaan haluttu kerros
        while self.kerros > siirtyma and siirtyma >= talo.alin_kerros:
            self.kerros += -1
            print(f"Hissi {hissi} meni kerrokseen {self.kerros}")
        print(f"Loppupiste: Hissi {hissi} on kerroksessa {self.kerros}")

class Talo():
    def __init__(self):
        self.alin_kerros = 1
        self.ylin_kerros = 10
        self.hissimaara = 3
        self.hissilista = []

        #Luodaan hissilistaan hissi-oliot
        while self.hissimaara > 0:
            hissi = Hissi()
            self.hissilista.append(hissi)
            self.hissimaara -= 1

    def aja_hissia(self, hissi, siirtyma):
        #Tarkistetaan mennäänkö ylös vai alas
        if siirtyma > self.hissilista[hissi].kerros:
            self.hissilista[hissi].siirry_ylos(siirtyma, hissi)
        elif siirtyma < self.hissilista[hissi].kerros:
            self.hissilista[hissi].siirry_alas(siirtyma, hissi)

    def palohalytys(self):
        #Ajetaan jokainen hissi listassa alas
        for each in talo.hissilista:
            talo.aja_hissia(talo.hissilista.index(each), talo.alin_kerros)

#Luodaan talo-olio
talo = Talo()

#Ajetaan hissiä 0 ylös
talo.aja_hissia(0, 10)

#Ajetaan hissiä 0 alas
talo.aja_hissia(0, 2)

#Ajetaan hissiä 1 ylös
talo.aja_hissia(1, 4)

#Ajetaan hissiä 2 alas, joka on jo alimmassa kerroksessa
talo.aja_hissia(2, 0)

#Kutsutaan palohälytys-metodia
talo.palohalytys()