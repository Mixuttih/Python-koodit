let numberArray = [312, 125, 21, 12, 55, 24, 75, 32, 99, 35, 76, 45, 44]

function even(array) {
    let evenArray = []
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            evenArray.push(array[i]);
        }
    }
    return evenArray
}

let newNumberArray = even(numberArray);
console.log("Original array: ");
console.log(numberArray);
console.log("Even array: ");
console.log(newNumberArray);
