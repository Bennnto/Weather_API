import requests
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

import os

load_dotenv()

def get_location(city: str):
    geolocation = Nominatim(user_agent="Weather")
    location = geolocation.geocode(city)
    name = city
    lat = location.latitude
    lon = location.longitude
    return name, lat, lon

def weather_info(lat:float, lon:float):
    API_KEY = os.getenv("APIKEY")
    URL = os.getenv("BASE_URL")
    params = {
        "appid": API_KEY,
        "lat" : lat,
        "lon" : lon,
        "units" : "metric",
    }
    response = requests.get(URL, params=params, timeout=20)
    if response.status_code == 200 :
        data = response.json()
        extract = extract_info(data)
        return extract
    else :
        response.raise_for_status()
        return

def extract_info(data):
    weather = {
        "city" : data.get("name", None),
        "temp" : data["main"]["temp"],
        "feels_like" : data["main"]["feels_like"],
        "temp_min" : data["main"]["temp_min"],
        "temp_max" : data["main"]["temp_max"],
        "pressure" : data["main"]["pressure"],
        "humidity" : data["main"]["humidity"],
        "sea_level" :  data["main"]["sea_level"],
        "ground_level" : data["main"]["grnd_level"],
        "wind_spd" : data["wind"].get("speed", None),
        "wind_deg" : data["wind"].get("deg", None),
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]

    }

    return weather



if __name__ == "__main__":
    get_location("toronto")
