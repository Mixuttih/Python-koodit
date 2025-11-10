function listaFunktio(i) {
    let listaTag = document.createElement("li");
    listaTag.innerText = i;
    document.getElementById("target").appendChild(listaTag);
}

let listaData = ["First item", "Second item", "Third item"]

listaData.forEach(listaFunktio);