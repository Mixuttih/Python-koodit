let button = document.getElementById("start")



button.addEventListener("click", calculateFunction)

function calculateFunction() {
    let value1 = document.getElementById("num1").value
    let value2 = document.getElementById("num2").value
    let resultArea = document.getElementById("result")

    let operation = document.getElementById("operation").value

    if (operation === "add") {
        resultArea.innerText = parseInt(value1) + parseInt(value2)
    }
    else if (operation === "sub") {
        resultArea.innerText = parseInt(value1) - parseInt(value2)
    }
    else if (operation === "multi") {
        resultArea.innerText = parseInt(value1) * parseInt(value2)
    }
    else if (operation === "div") {
        resultArea.innerText = parseInt(value1) / parseInt(value2)
    }
}