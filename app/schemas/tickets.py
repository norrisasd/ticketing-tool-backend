"""This module defines the schemas for the tickets."""
from enum import Enum
from pydantic import BaseModel


class Priority(str, Enum):
    """Represents a user role."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class TicketBase(BaseModel):
    """Represents a ticket."""
    title: str
    content: str
    status: str
    priority: Priority = Priority.LOW
    category_id: int
    created_by_id: int
    assigned_to_id: int | None = None


class CreateTicket(TicketBase):
    """Represents a ticket creation request."""
    pass


class TicketInDBBase(TicketBase):
    """
    Represents a ticket in the database.
    """
    id: int
    closed_at: str | None = None
    closed_by_id: int | None = None

    class Config:
        """Enable ORM mode."""
        from_attributes = True
