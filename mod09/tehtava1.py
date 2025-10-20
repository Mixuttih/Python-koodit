class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

auto1 = Auto("ABC-123", "142 km/h")

print(f"Rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus}")
print(f"Nopeus: {auto1.nopeus}")
print(f"Kuljettu matka: {auto1.kuljettumatka}")