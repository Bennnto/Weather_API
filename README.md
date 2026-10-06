## Weather API 

Weather API solution for [Weather API](https://roadmap.sh/projects/weather-api-wrapper-service) challenge from [roadmap.sh](https://roadmap.sh/dashboard)

- This project is a FastAPI based Weather API project that fetch weather information from [Openweathermap.org](https://openweathermap.org) based on a location
  name or coordinate (lattitude and longitude) this api included cache and rate limit
  - Cache use python-redis-cache library to minimize api requests
  - rate limit use ratelimit library in python to determined call limit within the period of time (10 calls in 30 minutes)
```
- Project Structure
  |
  ├── database.py - create database engine and session
  |
  ├── get_info.py - Helper function for API call and extract information from requests
  |
  ├── main.py - main application 
  |
  ├── models.py - SQL models (Location and Weather models)
  |
  ├── routes.py - API router (POST, GET)
  |
  └── schemas.py - Pydantic model from validate information
```

- API information
- Base URL
  ```
  http://localhost:8000/Weather/
  ```
- Documents OpenApi
  ```
  http://localhost:8000/docs/
  ```
- Response Example
```
{
  "location_id": 2,
  "temp": 22.22,
  "feel_likes": null,
  "temp_min": 21.59,
  "temp_max": 22.8,
  "pressure": 1006,
  "humidity": 78,
  "sea_lv": null,
  "grnd_lv": null,
  "wind_spd": 5.14,
  "wind_deg": null,
  "description": "clear sky"
}
```
