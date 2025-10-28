import requests
import json

saakone = True
api = "8aaee5bfe760d365fe7df353fce3e964"

while saakone == True:
    hakusana = input("Type a location for weather information: ")

    paikkahaku = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={hakusana}&appid={api}").json()
    haku = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={paikkahaku[0]["lat"]}&lon={paikkahaku[0]["lon"]}&appid={api}").json()
    print("Weather information:")
    print(haku["weather"][0]["main"])
    kelvin = haku["main"]["temp"]
    print(f"{round(kelvin - 273.15)}°C")
