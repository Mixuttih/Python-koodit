class Hissi():
    def __init__(self):
        self.alin_kerros = 1
        self.ylin_kerros = 10
        self.kerros = 1

    def siirry_kerrokseen(self, siirtyma):
        #Tarkastetaan mennäänkö ylös
        if siirtyma > self.kerros and siirtyma <= self.ylin_kerros:
            #Looppi kunnes kerros on saavutettu
            while siirtyma > self.kerros:
                #Mennään kerros ylös
                self.siirry_ylos()
                print(f"Siirrytty kerrokseen {self.kerros}")
            #Kun kerros saavutettu
            print(f"Kerros {self.kerros} saavutettu")

        #Tarkastetaan mennäänkö alas
        elif siirtyma < self.kerros and siirtyma >= self.alin_kerros:
            #Looppi kunnes kerros saavutettu
            while siirtyma < self.kerros:
                #Mennään kerros alas
                self.siirry_alas()
                print(f"Siirrytty kerrokseen {self.kerros}")
            #Kun kerros saavutettu
            print(f"Kerros {self.kerros} saavutettu")

        #Jos kerros on sama
        else:
            print(f"Kerros {self.kerros} saavutettu")

    def siirry_ylos(self):
        #Nostetaan kerrosta
        self.kerros += 1

    def siirry_alas(self):
        #Lasketaan kerrosta
        self.kerros += -1

#Luodaan olio
hissi = Hissi()

#Nostetaan hissi ylös
hissi.siirry_kerrokseen(10)

#Lasketaan hissi alas
hissi.siirry_kerrokseen(1)

#Koitetaan mennä olemattomaan kerrokseen, niin pysytään samassa kerroksessa
hissi.siirry_kerrokseen(11)