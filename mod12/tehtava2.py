import requests

#Loopin muuttuja
saakone = True
api = "KÄYTÄ OMAASI"

#Loputon loop
while saakone == True:
    #Paikkakunta jonka sää haetaan
    hakusana = input("Type a location for weather information: ")

    #Haetaan paikan sijainti
    paikkahaku = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={hakusana}&appid={api}").json()

    #Haetaan sijainnin perusteella sää
    haku = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={paikkahaku[0]["lat"]}&lon={paikkahaku[0]["lon"]}&appid={api}").json()

    #Printataan säätiedot
    print("Weather information:")

    #Sään tekstikuvaus
    print(haku["weather"][0]["main"])

    #Asetetaan lämpötila muuttujaan
    kelvin = haku["main"]["temp"]

    #Muutetaan lämpötila Celsius-asteiksi ja printataan
    print(f"{round(kelvin - 273.15)}°C")
