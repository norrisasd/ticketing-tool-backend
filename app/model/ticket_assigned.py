"""This modu"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class TicketAssignee(TimeStamp, Base):
    """Create a TicketCategoriesUser model to store ticket category data in the database."""
    __tablename__ = 'ticket_assignees'

    ticket_id = Column(Integer,  ForeignKey(
        "tickets.id"), index=True, primary_key=True, nullable=False)
    assignee_id = Column(Integer, ForeignKey("users.id"),
                         index=True, nullable=True)

    tickets = relationship("Tickets", back_populates="assigned_to")
    assigned_user = relationship("User", back_populates="assigned_to")
