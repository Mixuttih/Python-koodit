let button = document.getElementsByTagName("button")[0]

button.id = "button"

document.querySelector("button").addEventListener("click", showAlert)

function showAlert() {
    window.alert("Painoit nappia");
}