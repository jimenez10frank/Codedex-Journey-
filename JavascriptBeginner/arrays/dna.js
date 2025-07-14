const dnaPieces = ["A", "C", "G", "T"];

let myDNA = [];
for (let i = 0; i < 24; i++) {
    pieceOne = Math.floor(Math.random() * dnaPieces.length);
    pieceTwo = Math.floor(Math.random() * dnaPieces.length);
    pieceThree = Math.floor(Math.random() * dnaPieces.length);

    myDNA.push(dnaPieces[pieceOne] + dnaPieces[pieceTwo] + dnaPieces[pieceThree]);
}

console.log(myDNA);