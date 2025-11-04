function noppafunktio() {
    const minCeiled = Math.ceil(1);
    const maxFloored = Math.floor(7);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled)
}

let noppaheitot = []

while (noppaheitot[0] !== 6) {
    let noppa = noppafunktio();
    noppaheitot.unshift(parseInt(noppa));
}

function noppalistafunktio() {
    document.getElementById("noppalista").innerHTML += `<li>${noppaheitot[0]}</li>`
    noppaheitot.shift()
}

noppaheitot.forEach(noppalistafunktio);