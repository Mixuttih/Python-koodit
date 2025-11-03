function getRandomInt(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // The maximum is exclusive and the minimum is inclusive
}

let randomNumero = getRandomInt(1, 5);

if (randomNumero == 1) {
    document.querySelector("#randompaikka").innerHTML = `<h2>${nimi} on tuvassa Rohkelikko!</h2>`;
}
else if (randomNumero == 2) {
    document.querySelector("#randompaikka").innerHTML = `<h2>${nimi} on tuvassa Puuskupuh!</h2>`;
}
else if (randomNumero == 3) {
    document.querySelector("#randompaikka").innerHTML = `<h2>${nimi} on tuvassa Korpinkynsi!</h2>`;
}
else if (randomNumero == 4) {
    document.querySelector("#randompaikka").innerHTML = `<h2>${nimi} on tuvassa Luihunen!</h2>`;
}