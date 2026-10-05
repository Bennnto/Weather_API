from tempfile import tempdir

from pydantic import BaseModel


class Location_Base(BaseModel):
    name : str
    latitude : float
    longitude : float

class Location_Create(Location_Base):
    pass

class Location_Response(BaseModel):
    id : int
    name : str
    latitude : float
    longitude : float


class Weather_Base(BaseModel):
    location_id : int
    temp : float | None = None
    feel_likes : float | None = None
    temp_min : float | None = None
    temp_max : float | None = None
    pressure : float | None = None
    humidity : float | None = None
    sea_lv : float | None = None
    grnd_lv : float | None = None
    wind_spd : float | None = None
    wind_deg : float | None = None
    description : str | None = None

class Weather_Response(Weather_Base):
    pass

class Weather_Create(Weather_Base):
    pass
