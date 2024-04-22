"""This module defines the schema for the ticket category model."""
from pydantic import BaseModel


class TicketCategoryBase(BaseModel):
    """Represents a ticket category."""
    name: str


class TicketCategoryCreate(TicketCategoryBase):
    """Represents a ticket category creation request."""
    pass


class TicketCategoryResponse(BaseModel):
    """Represents a ticket category response."""
    categories: list[str]


class TicketCategoryInDBBase(TicketCategoryBase):
    """
    Represents a ticket category in the database.
    """
    id: int

    class Config:
        """Enable ORM mode."""
        from_attributes = True
