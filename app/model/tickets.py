"""This module contains the Tickets model."""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class Tickets(TimeStamp, Base):
    """Create a Tickets model to store ticket data in the database."""
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(Text, index=True)
    html = Column(Text, index=True)
    status = Column(String, index=True, nullable=False)
    priority = Column(String, index=True, nullable=False)

    created_by_id = Column(Integer, ForeignKey("users.id"),
                           index=True, nullable=False)

    category_id = Column(Integer, ForeignKey(
        "ticket_categories.id"), index=True, nullable=False)
    category = relationship("TicketCategories", back_populates="tickets")
    created_by = relationship("User", back_populates="created_tickets")
    closed_by = relationship(
        "TicketCloser", back_populates="tickets", cascade="all, delete-orphan")
    assigned_to = relationship(
        "TicketAssignee", back_populates="tickets", cascade="all, delete-orphan")
