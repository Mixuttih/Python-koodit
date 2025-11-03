let vuosiluku1 = parseInt(window.prompt("Mistä vuodesta haluat aloittaa?"))
let vuosiluku2 = parseInt(window.prompt("Mihin vuoteen haluat lopettaa?"))

function tarkistaVuosi(i) {
    if (i % 4 == 0) {
        if (i % 100 == 0) {
            return true;
        }
        return true;
    }
    return false;
}

karkausvuodet = []

while (vuosiluku1 < vuosiluku2) {
    let onkoKarkausvuosi = tarkistaVuosi(vuosiluku1);
        if (onkoKarkausvuosi == true) {
            karkausvuodet.push(vuosiluku1);
            vuosiluku1++
        }
        else {
            vuosiluku1++
        }
}

function listafunktio(value) {
  vuosilista += "<li>" + value + "</li>";
}

let vuosilista = "<ul>";
karkausvuodet.forEach(listafunktio);
vuosilista += "</ul>";

document.querySelector("#karkausvuosilista").innerHTML = `<h2>${vuosilista}</h2>`;

