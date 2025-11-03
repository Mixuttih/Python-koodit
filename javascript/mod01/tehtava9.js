let tarkistettavaNumero = parseInt(prompt("Syötä luku:"));
let onkoAlkuluku = true;

if (tarkistettavaNumero <= 1) {
    document.querySelector("#alkulukupaikka").innerHTML = `<h2>${tarkistettavaNumero} ei ole alkuluku</h2>`;
}
else if (tarkistettavaNumero > 1) {
    for (let i = 2; i <= tarkistettavaNumero/2; i++) {
        if (tarkistettavaNumero % i == 0) {
            onkoAlkuluku = false;
            break;
        }
    }

    if (onkoAlkuluku == true) {
        document.querySelector("#alkulukupaikka").innerHTML = `<h2>${tarkistettavaNumero} on alkuluku</h2>`;
    } else {
        document.querySelector("#alkulukupaikka").innerHTML = `<h2>${tarkistettavaNumero} ei ole alkuluku</h2>`;
    }
}
else {
    document.querySelector("#alkulukupaikka").innerHTML = `<h2>${tarkistettavaNumero} ei ole alkuluku</h2>`;
}
