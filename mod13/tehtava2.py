from flask import Flask, Response
import mariadb
import json

app = Flask(__name__)

conn = mariadb.connect(
         host='127.0.0.1',
         port= 3307,
         user='root',
         password='mikasana',
         database='flight_game')
cur = conn.cursor()

@app.route("/kentta/<koodi>")
def kentta(koodi):
    try:
        koodi = koodi
        cur.execute(f'''SELECT ident, name, municipality FROM airport WHERE ident = "{koodi}"''')
        tilakoodi = 200
        tulos = cur.fetchall()
        vastaus = {
            "ICAO": tulos[0][0],
            "Name": tulos[0][1],
            "Municipality": tulos[0][2]
        }
        jsonvast = json.dumps(vastaus)

    except IndexError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen haku"
        }
        jsonvast = json.dumps(vastaus)

    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run()