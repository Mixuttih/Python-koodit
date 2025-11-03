function getRandomInt(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // The maximum is exclusive and the minimum is inclusive
}

let montaNoppaa = parseInt(window.prompt("Montako noppaa haluaisit heittää?"))
let summaToive = parseInt(window.prompt("Minkä summan haluaisit niistä nopista?"))
let noppaHeitot2 = []

for (let i = 0; i < 10000; i++) {
    let noppienSumma = 0
    for (let j = 0; j < montaNoppaa; j++) {
        let nopanHeitto = getRandomInt(1,7);
        noppienSumma += nopanHeitto;
    }
    noppaHeitot2.push(noppienSumma);
}

let esiintymiset = 0

function tarkistusfunktio(i) {
    if (i == summaToive) {
        esiintymiset++
    }
}

noppaHeitot2.forEach(tarkistusfunktio)

console.log((esiintymiset/noppaHeitot2.length)*100+"%");
mahdollisuudet = (esiintymiset/noppaHeitot2.length)*100
document.querySelector("#mahdollisuuspaikka").innerHTML = `<h2>${mahdollisuudet.toFixed(2)}%</h2>`;
