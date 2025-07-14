const musicPlaylist = [
  "Tom Sawyer",
  "Sabotage",
  "I Wanna Dance With Somebody",
  "Don't Speak",
  "Bulls On Parade",
  "Thriller",
  "The Breaks",
  "Brick",
  "Aeroplane Over the Sea",
  "Tubthumping"
];

// here i remove the first element
let shiftedElement = musicPlaylist.shift();
// here i remove the last
let poppedElement = musicPlaylist.pop();
// here i add a new ellement at the end of the array
let first = "first element";
let unshiftElement = musicPlaylist.unshift(first);
// here i add an new element at the end of the array;
let end1 = "end first";
let end2 = "end second";
let pushElement = musicPlaylist.push(end1, end2);
// printing everything out
console.log(shiftedElement);
console.log(poppedElement);
console.log(unshiftElement);
console.log(pushElement);
console.log(musicPlaylist);