from fastapi import FastAPI, APIRouter, Response, HTTPException, Depends
from database import get_db
from schemas import Weather_Create, Weather_Response, Location_Create, Location_Response
from models import Location, Weather
from sqlalchemy.orm import Session
from get_info import get_location, weather_info
from redis import StrictRedis
from redis_cache import RedisCache
from typing import List
from ratelimit import limits

router = APIRouter()

client = StrictRedis(host="redis", decode_response=True)
cache = RedisCache(redis_client=client)

THIRTYMINUTES = 1800

@limits(calls=10, period=THIRTYMINUTES)
@router.post(f"/weather/", response_model=Weather_Response)
def post_weather(city: str, db: Session=Depends(get_db)):
    location = db.query(Location).filter(Location.name == city).first()
    if not location :
        api_location = get_location(city)
        if not api_location :
            raise HTTPException(status_code=401, detail="Cannot get location data from APIs")
        name, lat, lon = api_location
        location = Location(
            name = name,
            latitude = lat,
            longitude = lon,
        )
        db.add(location)
        db.commit()
        db.refresh(location)

    weather_data = weather_info(location.latitude, location.longitude)
    if weather_data is None :
        raise HTTPException(status_code=401, detail="Cannot get weather information from APIs")
    weather = Weather(
        location_id = location.id,
        temp = weather_data.get("temp", None),
        feels_like = weather_data.get("feels_like", None),
        temp_min = weather_data.get("temp_min", None),
        temp_max = weather_data.get("temp_max", None),
        pressure = weather_data.get("pressure", None),
        humidity = weather_data.get("humidity", None),
        sea_lv = weather_data.get("sea_lv", None),
        grnd_lv = weather_data.get("grnd_lv", None),
        wind_spd = weather_data.get("wind_spd", None),
        wind_deg = weather_data.get("wind_gust", None),
        description = weather_data.get("description", None),
    )
    db.add(weather)
    db.commit()
    db.refresh(weather)
    return weather

@limits(calls=10, period=THIRTYMINUTES)
@cache.cache()
@router.get("/weather/", response_model=List[Weather_Response])
def get_weather(db : Session = Depends(get_db)):
    weather = db.query(Weather).all()
    return weather

@limits(calls=10, period=THIRTYMINUTES)
@cache.cache()
@router.get("/weather/{city}/", response_model=Weather_Response)
def get_weather_city(city: str, db: Session=(Depends(get_db))):
    location = db.query(Location).filter(Location.name == city).first()
    if location is not None :
        weather = db.query(Weather).filter(Weather.location_id == location.id).first()
        return weather
    else:
        raise HTTPException(status_code=400, detail="Not found weather information in database")
