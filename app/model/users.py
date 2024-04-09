"""Create a User model to store user data in the database."""
from sqlalchemy import Column, Integer, String
from app.config import Base
from app.model.mixins import TimeStamp


class User(TimeStamp, Base):
    """function to create a User model ."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, unique=True, index=True)
    hash_password = Column(String)
