const form = document.getElementById("weather-form");
const cityInput = document.getElementById("city_input");
const resultDiv = document.getElementById("result");
const errDiv = document.getElementById("error");
const loadingDiv = document.getElementById("loading");
const iconImg = document.getElementById("weather-icon");

async function searchWeather(city) {
  if (!city) return;

  errDiv.classList.add("hidden");
  resultDiv.classList.add("hidden");
  loadingDiv.classList.remove("hidden");

  try {
    const response = await fetch(`/weather/?city=${encodeURIComponent(city)}`, {
      method: "POST"
    });

    if (!response.ok) {
      throw new Error(`City "${city}" not found or service unavailable.`);
    }

    const data = await response.json();

    // Render weather icon
    if (data.icon) {
      iconImg.src = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
      iconImg.classList.remove("hidden");
    } else {
      iconImg.classList.add("hidden");
    }

    // Safely populate values
    document.getElementById("display-city").textContent = city;
    document.getElementById("temp-val").textContent = `${Math.round(data.temp)}°C`;
    document.getElementById("description").textContent = data.description || "";

    const feelsLikeEl = document.getElementById("feels-like-val");
    if (feelsLikeEl) {
      feelsLikeEl.textContent = data.feels_like != null ? `${Math.round(data.feels_like)}°C` : "--";
    }

    const humidityEl = document.getElementById("humidity-val");
    if (humidityEl) {
      humidityEl.textContent = data.humidity != null ? data.humidity : "--";
    }

    const windEl = document.getElementById("wind-val");
    if (windEl) {
      windEl.textContent = data.wind_spd != null ? data.wind_spd : "--";
    }

    const pressureEl = document.getElementById("pressure-val");
    if (pressureEl) {
      pressureEl.textContent = data.pressure != null ? data.pressure : "--";
    }

    resultDiv.classList.remove("hidden");
  } catch (err) {
    errDiv.textContent = err.message;
    errDiv.classList.remove("hidden");
  } finally {
    loadingDiv.classList.add("hidden");
  }
}

// Form submit handler
form.addEventListener("submit", (e) => {
  e.preventDefault();
  searchWeather(cityInput.value.trim());
});

// Quick city buttons handler
document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    cityInput.value = chip.textContent;
    searchWeather(chip.textContent);
  });
});
