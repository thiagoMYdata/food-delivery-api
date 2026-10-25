from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import engine
from app.config.app_config import getApp_config
from typing import Generator

Base = declarative_base()
db_url = getApp_config().db_url
engine = engine.create_engine(db_url)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


