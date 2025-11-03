let lasketaankoNeliojuuri = window.confirm("Lasketaanko neliöjuuri?")

if (lasketaankoNeliojuuri == true) {
    let laskettavaLuku = window.prompt("Syötä luku:")

    if (parseInt(laskettavaLuku) >= 0) {
        let neliojuuri = Math.sqrt(parseInt(laskettavaLuku))
        document.querySelector("#neliojuuripaikka").innerHTML = `<h2>${laskettavaLuku}:n neliöjuuri on ${neliojuuri}</h2>`;
    }
    else {
        document.querySelector("#neliojuuripaikka").innerHTML = `<h2>Neliöjuurta ei voi laskea negatiivisesta luvusta</h2>`;
    }
}
else {
    document.querySelector("#neliojuuripaikka").innerHTML = `<h2>Neliöjuurta ei laskettu</h2>`;
}