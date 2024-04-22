"""This module contains the User schema."""
from enum import Enum
from pydantic import BaseModel


class UserRole(str, Enum):
    """Represents a user role."""
    ADMIN = "admin"
    USER = "user"
    AGENT = "agent"


class Token(BaseModel):
    """Represents a token."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Represents token data."""
    username: str | None = None


class UserBase(BaseModel):
    """Represents a user."""
    username: str
    email: str | None = None
    full_name: str | None = None
    role: UserRole = UserRole.USER


class UserInDBBase(UserBase):
    """
    Represents a user in the database.
    """

    id: int

    class Config:
        """Enable ORM mode."""
        from_attributes = True


class CreateUser(UserBase):
    """Represents a user creation request."""
    password: str


class UserInDB(UserBase):
    """Represents a user in the database."""
    hashed_password: str


class UserLogin(BaseModel):
    """Represents a user login request."""
    username: str
    password: str
