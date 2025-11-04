let uusiNumeroArray = []
let taasUusiNumero = window.prompt("Syötä numero:")

while (uusiNumeroArray.includes(parseInt(taasUusiNumero)) === false) {

    //Jos käyttäjä syöttää jotain muuta kuin numeron
    //TAI
    //Jos käyttäjä yrittää syöttää numeron joka on jo listassa, kun kysytään numeroa uudelleen
       while (isNaN(parseInt(taasUusiNumero)) || uusiNumeroArray.includes(parseInt(taasUusiNumero)) === true) {
           taasUusiNumero = window.prompt("Syötä oikea numero:")
       }

    uusiNumeroArray.unshift(parseInt(taasUusiNumero))
    taasUusiNumero = window.prompt("Syötä numero:")
}

console.log(uusiNumeroArray)