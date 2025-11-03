let numero1 = window.prompt("Syötä ensimmäinen kokonaisluku:")
let numero2 = window.prompt("Syötä toinen kokonaisluku:")
let numero3 = window.prompt("Syötä kolmas kokonaisluku:")

let summa = parseInt(numero1)+parseInt(numero2)+parseInt(numero3);
let tulo = parseInt(numero1)*parseInt(numero2)*parseInt(numero3);
let keskiarvo = summa / 3;

document.querySelector("#laskupaikka").innerHTML = `<h2>Sum: ${summa}, Product: ${tulo}, Average: ${keskiarvo}</h2>`;