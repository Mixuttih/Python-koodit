let osallistujaMaara = parseInt(window.prompt("Kuinka monta osallistujaa?"))
let osallistujaLista = []

for (let i = 1; i <= osallistujaMaara; i++) {
    let osallistujaNimi = window.prompt(`Syötä osallistujan ${i}. nimi:`)
    osallistujaLista.push(osallistujaNimi)
}

osallistujaLista.sort()

function osallistujaFunktio(item) {
    document.getElementById("osallistujalista").innerHTML += `<li>${item}</li>`
}

osallistujaLista.forEach(osallistujaFunktio)

