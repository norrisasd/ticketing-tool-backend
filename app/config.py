"""Configuration of database connection and session management."""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import logging

load_dotenv(find_dotenv())

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

SQLALCHEMY_DATABASE_URL = "postgresql://" + db_user + ":" + \
    db_password + "@db/" + db_name

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
logger = logging.getLogger(__name__)


def get_db():
    """This function returns a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
