"""Create a User model to store user data in the database."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class User(TimeStamp, Base):
    """function to create a User model ."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, unique=True, index=True)
    role = Column(String, index=True, nullable=False)
    hash_password = Column(String)

    categories = relationship("TicketCategoriesUser", back_populates="user")
    # created_tickets = relationship("Tickets", back_populates="created_by")
    # assigned_tickets = relationship("Tickets", back_populates="assigned_to")
    # closed_tickets = relationship("Tickets", back_populates="closed_by")
