let nimi = window.prompt("Mikä on nimesi?")

document.querySelector("#nimipaikka").innerHTML = `<h2>Hello ${nimi}!</h2>`;