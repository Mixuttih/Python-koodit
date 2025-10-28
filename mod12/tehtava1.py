import requests

vitsikone = True

while vitsikone == True:
    input("Press enter to Chuck Norris...")
    vitsi = requests.get("https://api.chucknorris.io/jokes/random").json()
    print(vitsi["value"])
