function noppafunktio2(max) {
    const minCeiled = Math.ceil(1);
    const maxFloored = Math.floor(max+1);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled)
}

let noppaheitot2 = []
let nopansivut = parseInt(window.prompt("TEHTÄVÄ 7: Kuinka monta lukua nopassa on?"))

while (noppaheitot2[0] !== nopansivut) {
    let noppa2 = noppafunktio2(nopansivut);
    noppaheitot2.unshift(parseInt(noppa2));
}

function noppalistafunktio2() {
    document.getElementById("noppalista2").innerHTML += `<li>${noppaheitot2[0]}</li>`
    noppaheitot2.shift()
}

noppaheitot2.forEach(noppalistafunktio2);


