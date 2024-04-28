"""This module defines the schemas for the tickets."""
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Priority(str, Enum):
    """Represents a user role."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Status(str, Enum):
    """Represents a ticket status."""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"


class TicketBase(BaseModel):
    """Represents a ticket."""
    title: str
    content: str
    status: Status = Status.OPEN
    priority: Priority = Priority.LOW
    category_id: int
    created_by_id: int


class TicketResponse(BaseModel):
    """Represents a ticket response."""
    id: int
    title: str
    content: str
    status: Status
    priority: Priority
    category: str
    created_by: str
    assigned_to: str | None = None
    created_at: datetime
    updated_at: str | None = None
    closed_at: datetime | None = None
    closed_by: str | None = None


class CreateTicket(TicketBase):
    """Represents a ticket creation request."""
    assigned_to_id: int | None = None


class AssignTicket(BaseModel):
    """Represents a ticket assignment request."""
    id: int
    assigned_to: int


class CloseTicket(BaseModel):
    """Represents a ticket close request."""
    id: int
    closed_by: int


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
