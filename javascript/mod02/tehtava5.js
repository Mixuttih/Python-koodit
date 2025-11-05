let uusiNumeroArray = []
let taasUusiNumero = window.prompt("TEHTÄVÄ 5: Syötä numero:")

while (uusiNumeroArray.includes(parseInt(taasUusiNumero)) === false) {

    //Jos käyttäjä syöttää jotain muuta kuin numeron
   while (isNaN(parseInt(taasUusiNumero)) === true && uusiNumeroArray.includes(parseInt(taasUusiNumero)) === false) {
       taasUusiNumero = window.prompt("Syötä oikea numero:")
   }

   //Jos käyttäjä yrittää syöttää numeron joka on jo listassa, kun kysytään numeroa uudelleen
   if (uusiNumeroArray.includes(parseInt(taasUusiNumero)) === true) {
       break
   }

    uusiNumeroArray.unshift(parseInt(taasUusiNumero))
    taasUusiNumero = window.prompt("Syötä numero:")
}
uusiNumeroArray.sort(function(a, b) {return a - b;})
console.log(uusiNumeroArray)