#2 Tietokannan kyselyn tulkitseminen
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='mikasana',
         autocommit=True
         )



def tietokantahaku(i):
    sql = f"SELECT type FROM airport where iso_country='{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    heliports = 0
    small_airports = 0
    medium_airports = 0
    large_airports = 0
    closed = 0

    if kursori.rowcount > 0:
        for rivi in tulos:
            if rivi[0] == "heliport":
                heliports += 1
            elif rivi[0] == "small_airport":
                small_airports += 1
            elif rivi[0] == "medium_airport":
                medium_airports += 1
            elif rivi[0] == "large_airport":
                large_airports += 1
            elif rivi[0] == "closed":
                closed += 1
    print(f"Maassa {i} on:")
    print(f"{heliports} helikopterikenttää")
    print(f"{small_airports} pientä lentokenttää")
    print(f"{medium_airports} keskikokoista lentokenttää")
    print(f"{large_airports} isoa lentokenttää")
    print(f"{closed} suljettua lentokenttää.")
    return

koodi = input("Syötä maa-koodi: ")
tietokantahaku(koodi)