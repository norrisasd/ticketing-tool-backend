"""This module contains the JSON response Schema."""
from pydantic import BaseModel


class Response(BaseModel):
    """Represents a response."""
    status: int
    message: str


class LoginResponse(Response):
    """Represents a login response."""
    access_token: str
    token_type: str
