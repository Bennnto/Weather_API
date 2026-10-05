from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,  sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()
