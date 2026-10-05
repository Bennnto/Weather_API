from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, ForeignKey,  String, DateTime, Text
from datetime import datetime
from database import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    weather = relationship("Weather" ,back_populates="location", cascade="all, delete-orphan")


class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="CASCADE"))
    temp = Column(Float, nullable=True)
    feels_like = Column(Float, nullable=True)
    temp_min = Column(Float, nullable=True)
    temp_max = Column(Float, nullable=True)
    pressure = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    sea_lv = Column(Float, nullable=True)
    grnd_lv = Column(Float, nullable=True)
    wind_spd = Column(Float, nullable=True)
    wind_deg = Column(Float, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    location = relationship("Location", back_populates="weather")
