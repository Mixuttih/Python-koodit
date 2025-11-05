let candidates = parseInt(window.prompt("How many candidates?"))
let candidateList = []

for (let i = 1; i <= candidates; i++) {
    let candidateName = window.prompt(`Enter name of candidate #${i}.:`)
    candidateList.push({name: candidateName, votes: 0})
}

let voters = parseInt(window.prompt("How many voters?"))

for (let i = 1; i <= voters; i++) {
    let voterChoice = window.prompt(`Voter #${i}: Enter name of candidate to vote?`)

    function voteFunction(value) {
        if (voterChoice === value.name) {
            value.votes++
        }
    }

    candidateList.forEach(voteFunction)
}

candidateList.sort((a, b) => {console.log(a.votes, b.votes); return b.votes - a.votes;})
console.log("The winner is "+candidateList[0].name+" with "+candidateList[0].votes+" votes!")
console.log("Results:")

function resultFunction(value) {
    console.log(value.name+": "+value.votes+" votes")
}

candidateList.forEach(resultFunction)