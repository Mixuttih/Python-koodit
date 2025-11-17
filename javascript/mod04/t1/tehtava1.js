const tvmazeForm = document.querySelector('#tvmaze-form')
tvmazeForm.addEventListener('submit', async function(evt) {
    evt.preventDefault();

    const code = document.querySelector('input[name=q]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        const jsonData = await response.json();

        let resultarea = document.getElementById('results');
        resultarea.innerHTML = '';
        resultarea.innerHTML += '<h1>Results:</h1><br>';

        //Funktio foreach -komennolle
        function resultfunktio(i) {
            //Luodaan artikkeli
            let newArticle = document.createElement('article');

            //Luodaan otsikkoalue ja nimi muuttujaan
            let newHeading = document.createElement('h2');
            let newName = i.show.name;
            newHeading.append(newName)

            //Luodaan linkkialue, attribuutit ja linkki muuttujaan
            let newA = document.createElement("a");
            newA.setAttribute('href', `${i.show.url}`);
            newA.setAttribute('target', '_blank');
            let newUrl = i.show.url;
            newA.append(newUrl)

            //Rivinvaihto linkin jälkeen
            newA.insertAdjacentHTML("beforeend", "<br>")

            //Luodaan kuva-alue ja attribuutit
            let newImg = document.createElement('img');
            newImg.setAttribute('src', i.show.image?.medium);

            //Luodaan kuvausalue ja kuvaus muuttujaan
            let newDesc = document.createElement('div');
            let newDescription = i.show.summary;

            //Lisätään kuvaus alueelle, mutta sisällytetään HTML tag
            newDesc.insertAdjacentHTML( 'beforeend', newDescription )

            //Lyödään kaikki data articleen
            newArticle.append(newHeading, newA, newImg, newDesc);
            //Lyödään article sivulle
            resultarea.append(newArticle);
        }

        jsonData.forEach(resultfunktio)

    } catch (error) {
        console.log(error.message);
    }
});