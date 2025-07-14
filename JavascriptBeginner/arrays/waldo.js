const characters = [
  "The Wally Watchers",
  "Wilma",
  "Fritz",
  "Wizard Whitebeard",
  "Odlaw",
  "Waldo",
  "Woof"
];

if (characters.includes("Waldo")) {
    let waldoIndex = characters.indexOf("Waldo");
    console.log("we found Waldo at index " + waldoIndex);
} else {
    console.log("Not Found");
}