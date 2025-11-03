function getRandomInt(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // The maximum is exclusive and the minimum is inclusive
}


let noppaMaara = window.prompt("Monta kertaa haluat heittää noppaa?")
let noppaSumma = 0
let noppaHeitot = []

while (parseInt(noppaMaara) > 0) {
    let noppaluku = getRandomInt(1,7);
    noppaSumma += noppaluku;
    noppaHeitot.push(noppaluku);
    noppaMaara--
}

document.querySelector("#noppapaikka").innerHTML = `<h2>Nopanheittojen yhteenlaskettu summa on: ${noppaSumma} (${noppaHeitot})</h2>`;