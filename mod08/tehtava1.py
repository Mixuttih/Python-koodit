#1 Tietokantahaku
import mysql.connector

#Yhteysmuuttuja
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='mikasana',
         autocommit=True
         )

#Hakufunktio
def tietokantahaku(i):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]} on lentokenttä joka sijaitsee kaupungissa {rivi[1]}.")
    return

#Käyttäjäsyöte
koodi = input("Syötä ICAO -koodi: ")
tietokantahaku(koodi)