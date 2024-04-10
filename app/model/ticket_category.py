"""This module contains the TicketCategories model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class TicketCategories(TimeStamp, Base):
    """Create a TicketCategories model to store ticket category data in the database."""
    __tablename__ = 'ticket_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    users = relationship("TicketCategoriesUser", back_populates="category")
    tickets = relationship("Tickets", back_populates="category")
