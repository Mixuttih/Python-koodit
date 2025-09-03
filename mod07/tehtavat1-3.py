#1: vuodenaika kuukauden numerosta
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausi = input("Anna kuukauden järjestysnumero (1-12): ")
vuodenaika = vuodenajat[int(kuukausi)-1]
print (f"{kuukausi}. kuukausi on {vuodenaika}.")

#2: nimilista johon lisätään nimiä ja tulostetaan lopuksi
nimilista = {""} #Set ilman arvoja on dictionary
nimilista.remove("") #Poistetaan ylimääräinen arvo

nimi = input("Syötä nimi: ")

while nimi != "":
    if nimi in nimilista:
        print("Aiemmin syötetty nimi")
        nimi = input("Syötä nimi: ")
    else:
        print("Uusi nimi")
        nimilista.add(nimi)
        nimi = input("Syötä nimi: ")

for i in nimilista:
    print(i)

#3: lentokenttien haku- ja syöttöjärjestelmä
lentokentat = {
    "EFHK":"Helsinki-Vantaa Airport",
    "EFHF":"Helsinki-Malmi Airport",
    "EFHV":"Hyvinkää Airport",
    "EFOU":"Oulu Airport"
}

print("Kirjoita [SYÖTÄ] jos haluat syöttää uuden lentokentän tiedot.")
print("Kirjoita [HAE] jos haluat hakea lentokentän tietoja.")
print("Kirjoita [LOPETA] jos haluat lopettaa")
tilanne = input("[SYÖTÄ][HAE][LOPETA]: ")

#Prosessi joka pyörii kunnes käyttäjä antaa komennon "lopeta"
while tilanne.upper() != "LOPETA":
    #Prosessissa on 2 aktiivista tilaa, syöttö ja haku
    #Syöttötila
    if tilanne.upper() == "SYÖTÄ":
        kentan_nimi = input("Syötä uuden lentokentän nimi: ")
        kentan_koodi = input("Syötä uuden lentokentän ICAO -koodi: ").upper()
        lentokentat[kentan_koodi] = kentan_nimi
        #Käyttäjä voi vaihtaa prosessin tilaa
        tilanne = input("[SYÖTÄ][HAE][LOPETA]: ")
    #Hakutila
    if tilanne.upper() == "HAE":
        kentan_koodi = input("Syötä haettavan lentokentän ICAO -koodi: ").upper()
        #Etsitään syötettyä koodia
        if kentan_koodi in lentokentat:
            print(f"{kentan_koodi} -koodin lentokenttä on {lentokentat[kentan_koodi]}.")
            tilanne = input("[SYÖTÄ][HAE][LOPETA]: ")
        else:
            print("Haettua lentokenttää ei löydy")
            tilanne = input("[SYÖTÄ][HAE][LOPETA]: ")

    #Jos käyttäjä ei syötä oikeaa toimintoa
    else:
        print("Virhe! Syötettyä toimintoa ei ole.")
        tilanne = input("[SYÖTÄ][HAE][LOPETA]: ")

#Prosessi lopetettu
print("Ohjelma lopetettu.")