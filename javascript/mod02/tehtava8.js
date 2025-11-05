let stringArray = ["Eka sana", "Toka sana", "Kolmas sana", "Neljäs sana"];

function concat(array) {
    let newArray = [""];

    for (let i = 0; i < array.length; i++) {
        newArray[0] += array[i];
    }
    return newArray;
}

let concatArray = concat(stringArray);
document.getElementById("concatpaikka").innerHTML += concatArray;