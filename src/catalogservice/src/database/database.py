from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
DATABASE_NAME = os.environ.get("database_name")
DATABASE_USERNAME = os.environ.get("database_username")
DATABASE_PASSWORD = os.environ.get("database_password")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@postgres:5432/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)
Base = declarative_base()


def get_db():
    return Session()
