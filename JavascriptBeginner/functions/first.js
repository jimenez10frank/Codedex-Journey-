function greetings() {
  const randomNumber = Math.floor(Math.random() * 4) + 1;

  if (randomNumber == 1) {
    console.log("Howdy!");
    console.log(randomNumber);
  } else if (randomNumber == 2) {
    console.log("Hi there!");
    console.log(randomNumber);
  } else if (randomNumber == 3) {
    console.log("Hey what's happening?");
    console.log(randomNumber);
  } else if (randomNumber == 4) {
    console.log("Hola!");
    console.log(randomNumber);
  } else {
    console.log("Heya!");
    console.log(randomNumber);
  }
}

greetings();
greetings();
greetings();