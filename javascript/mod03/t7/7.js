let kuva = document.getElementById("target")
let trigger = document.getElementById("trigger")

trigger.addEventListener("mouseover", (eent) => {
    kuva.src = "img/picB.jpg"
})

trigger.addEventListener("mouseout", (eent) => {
    kuva.src = "img/picA.jpg"
})