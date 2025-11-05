regularArray = []
reversedArray = []

for (let i = 0; i < 5; i++) {
    let arrayData = window.prompt("TEHTÄVÄ 1: Syötä numero:")
    regularArray.push(arrayData)
}

function reverseAnArray(item) {
    reversedArray.unshift(item)
}

regularArray.forEach(reverseAnArray);

console.log(reversedArray)