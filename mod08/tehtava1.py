#1 Tietokantahaku
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
    sql = f"SELECT name, municipality FROM airport where ident='{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]} on lentokenttä joka sijaitsee kaupungissa {rivi[1]}.")
    return

koodi = input("Syötä ICAO -koodi: ")
tietokantahaku(koodi)