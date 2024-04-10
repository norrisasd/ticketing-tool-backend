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
    created_by = relationship("User", back_populates="created_tickets")

    assigned_to_id = Column(Integer, ForeignKey("users.id"),
                            index=True, nullable=True)
    assigned_to = relationship("User", back_populates="assigned_tickets")

    closed_at = Column(String, index=True, nullable=False)
    closed_by_id = Column(Integer, ForeignKey("users.id"),
                          index=True, nullable=True)
    closed_by = relationship("User", back_populates="closed_tickets")

    category_id = Column(Integer, ForeignKey(
        "ticket_categories.id"), index=True, nullable=False)
    category = relationship("TicketCategories", back_populates="tickets")
