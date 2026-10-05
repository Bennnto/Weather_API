from fastapi import FastAPI
from routes import router as weather_router
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(weather_router)
