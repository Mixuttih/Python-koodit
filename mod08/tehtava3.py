#3 Geopy tehtävä
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

def tietokantahaku(i):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{i}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            return rivi
    else:
        return None

eka_kentta = input("Syötä ensimmäisen lentokentän ICAO -koodi: ")
toka_kentta = input("Syötä toisen lentokentän ICAO -koodi: ")
eka_koordinaatit = tietokantahaku(eka_kentta)
toka_koordinaatit = tietokantahaku(toka_kentta)


from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="airport_haku")

location_1 = geolocator.reverse(f"{eka_koordinaatit[0]},{eka_koordinaatit[1]}")
location_2 = geolocator.reverse(f"{toka_koordinaatit[0]},{toka_koordinaatit[1]}")

print(f"Matkaa kahden lentokentän välillä on ~{int(distance.distance(eka_koordinaatit, toka_koordinaatit).km)} kilometriä")