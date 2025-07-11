const readline = require("readline");

// Define the zodiac signs and their corresponding months
const zodiacSigns = {
  January: ["♑", "Capricorn"],
  February: ["♒", "Aquarius"],
  March: ["♓", "Pisces"],
  April: ["♈", "Aries"],
  May: ["♉", "Taurus"],
  June: ["♊", "Gemini"],
  July: ["♋", "Cancer"],
  August: ["♌", "Leo"],
  September: ["♍", "Virgo"],
  October: ["♎", "Libra"],
  November: ["♏", "Scorpio"],
  December: ["♐", "Sagittarius"],
};

// List of possible fortunes
const fortunes = [
  "You will have a day filled with unexpected surprises!",
  "A great opportunity will present itself soon.",
  "Your hard work will pay off in the near future.",
  "An old friend will reenter your life.",
  "You'll make an important decision that will change your path.",
  "A long-awaited wish will finally come true.",
  "Your creativity will lead you to success.",
  "A period of personal growth is on the horizon.",
  "You'll discover a hidden talent you never knew you had.",
  "Love and happiness are just around the corner.",
];

// Function to get a random fortune
function getRandomFortune() {
  return fortunes[Math.floor(Math.random() * fortunes.length)];
}

// Function to generate horoscope
function generateHoroscope(birthMonth) {
  birthMonth =
    birthMonth.charAt(0).toUpperCase() + birthMonth.slice(1).toLowerCase();

  if (zodiacSigns.hasOwnProperty(birthMonth)) {
    const [symbol, sign] = zodiacSigns[birthMonth];
    const fortune = getRandomFortune();

    console.log(`Your zodiac sign is ${symbol} ${sign}.`);
    console.log(`Your horoscope for today: ${fortune}`);
  } else {
    console.log("Invalid month. Please enter a valid month name.");
  }
}

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Prompt user for input
rl.question("Enter the month you were born in: ", (birthMonth) => {
  generateHoroscope(birthMonth);
  rl.close();
});