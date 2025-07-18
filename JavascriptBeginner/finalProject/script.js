// function for the api
async function fetchWeather(){
    // select the search input
    let searchInput = document.getElementById("search").value;
    // her it selects the data that will be printed out
    const weatherDataSection = document.getElementById("weather-data");
    // here it changes it from display none to block
    weatherDataSection.style.display = "flex";
    // your api key:)
    const apiKey = "your own api";
    // error handling for when empty search
    if(searchInput == "") {
        weatherDataSection.innerHTML = `
        <div>
            <h2>Empty Input!</h2>
            <p>Please Try Again with a valid <u>city name</u>.</p>
        </div>
        `;
        return;
    }
    // function to get longitude and latitude

    async function getLonAndLat() {
        // countrycode
        const countryCode = 1;
        // url for geocode
        const geocodeURL = `https://api.openweathermap.org/geo/1.0/direct?q=${searchInput.replace(" ", "%20")},${countryCode}&limit=1&appid=${apiKey}`;
        // here i fetch the date with error handling
        const response = await fetch(geocodeURL);
        if(!response.ok) {
            console.log("Bad response!", response.status);
            return;
        }
        // also another error handling for the json data fetch
        const data = await response.json();
        if(data.length == 0) {
            console.log("Something went wrong here.");
            weatherDataSection.innerHTML = `
            <div>
            <h2>Invalid Input: "${searchInput}"</h2>
            <p>Please try again with a valid <u>city name</u>.</p>
            </div>
            `;
            return;
        } else {
            return data[0];
        }
    }

    // here i get the weather data
    async function getWeatherData(lon, lat) {
        const weatherURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`;
        // fetch error handling
        const response = await fetch(weatherURL);
        if(!response.ok) {
            console.log("Bad response!", response.status);
            return;
        }

        const data = await response.json();

        // here i display the data
        weatherDataSection.innerHTML = `
        <img src="https://openweathermap.org/img/wn/${data.weather[0].icon}.png" alt="${data.weather[0].description}" width="100" />
        <div>
          <h2>${data.name}</h2>
          <p><strong>Temperature:</strong> ${Math.round(data.main.temp - 273.15)}°C</p>
          <p><strong>Description:</strong> ${data.weather[0].description}</p>
          <p><strong>Description:</strong> ${data.wind.speed}</p>
        </div>
        `;
    }
    
    document.getElementById("search").value = "";
    const geocodeData = await getLonAndLat();
    getWeatherData(geocodeData.lon, geocodeData.lat);
}