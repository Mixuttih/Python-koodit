let koiraLista = []

for (let i = 1; i < 7; i++) {
    let koiraNimi = window.prompt(`TEHTÄVÄ 3: Syötä koiran ${i}. nimi:`)
    koiraLista.push(koiraNimi)
}

koiraLista.sort()

for (let i = 0; i < 6; i++) {
    document.getElementById("koiralista").innerHTML += `<li>${koiraLista[koiraLista.length - 1]}</li>`
    koiraLista.pop()
}
