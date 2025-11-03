function tarkistaVuosi(i) {
    if (i % 4 == 0) {
        if (i % 100 == 0) {
            return true;
        }
        return true;
    }
    return false;
}

let vuosi = window.prompt("Syötä vuosiluku:")

let karkausvuosi = tarkistaVuosi(parseInt(vuosi));
if (karkausvuosi == true) {
    document.querySelector("#vuosipaikka").innerHTML = `<h2>${vuosi} on karkausvuosi</h2>`;
}
else {
    document.querySelector("#vuosipaikka").innerHTML = `<h2>${vuosi} ei ole karkausvuosi</h2>`;
}
