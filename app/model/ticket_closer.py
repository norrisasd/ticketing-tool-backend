"""This module contains the TicketCloser model."""
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class TicketCloser(TimeStamp, Base):
    """Create a TicketCategoriesUser model to store ticket category data in the database."""
    __tablename__ = 'ticket_closers'

    ticket_id = Column(Integer, ForeignKey(
        "tickets.id"), index=True, primary_key=True, nullable=False)
    closed_by_id = Column(Integer, ForeignKey("users.id"),
                          index=True, nullable=True)
    closed_at = Column(DateTime, index=True, nullable=True)

    tickets = relationship("Tickets", back_populates="closed_by")
    closed_by_user = relationship("User", back_populates="closed_by")
