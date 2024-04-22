"""This module contains the User schema."""
from pydantic import BaseModel


class Response(BaseModel):
    """Represents a response."""
    status: int
    message: str
