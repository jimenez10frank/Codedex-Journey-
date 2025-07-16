const car = {
    model: "tesla",
    year: 2020,
    color: "blue",
    used: false
}

if(car.used == true) {
    console.log("Im looking for a 2024 " + car.model + " that is Used");
} else {
    console.log("Im looking for a 2024 " + car.model + " that is new");
}