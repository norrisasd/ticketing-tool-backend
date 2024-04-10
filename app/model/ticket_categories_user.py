"""This module contains the TicketCategoriesUser model."""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.config import Base
from app.model.mixins import TimeStamp


class TicketCategoriesUser(TimeStamp, Base):
    """Create a TicketCategoriesUser model to store ticket category data in the database."""
    __tablename__ = 'ticket_categories_users'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey(
        "ticket_categories.id"), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"),
                     index=True, nullable=False)

    category = relationship("TicketCategories", back_populates="users")
    user = relationship("User", back_populates="categories")
