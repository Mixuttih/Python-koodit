#2 Tietokannan kyselyn tulkitseminen
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
    sql = f"SELECT COUNT(type), type FROM airport WHERE iso_country='{i}' GROUP BY type ORDER BY COUNT(type) DESC"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        print(f"{i} airports are: ")
        for rivi in tulos:
            print(rivi[0], rivi[1])
    return

koodi = input("Enter Region code: ")
tietokantahaku(koodi)