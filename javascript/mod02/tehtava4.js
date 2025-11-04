let numeroArray = []
while (numeroArray[0] !== 0) {
    let uusiNumero = window.prompt("Syötä numero:")

        //Jos käyttäjä syöttää jotain muuta kuin numeron
       while (isNaN(parseInt(uusiNumero))) {
           uusiNumero = window.prompt("Syötä oikea numero:")
       }

       numeroArray.unshift(parseInt(uusiNumero))
}

numeroArray.sort(function(a, b){return b-a})

console.log(numeroArray)