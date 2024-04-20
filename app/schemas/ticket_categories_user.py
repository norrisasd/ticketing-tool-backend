"""This module defines the schema for the ticket category model."""
from pydantic import BaseModel


class TicketCategoryUserBase(BaseModel):
    """Represents a ticket category."""
    user_id: int
    category_id: int


class CreateTicketCategoryUser(TicketCategoryUserBase):
    """Represents a ticket category creation request."""
    pass


class TicketCategoryUserInDBBase(TicketCategoryUserBase):
    """
    Represents a ticket category in the database.
    """
    id: int

    class Config:
        """Enable ORM mode."""
        from_attributes = True
