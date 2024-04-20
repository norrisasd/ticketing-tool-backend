"""This module contains the security functions for the application authentication."""
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "be2a718af3ccfbff6f5d7200827866b42f293eb0ecc0b38fff4bc55fc52ab992"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify the plain password against the hashed password.

    Args:
        plain_password (str): The plain password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Get the hashed password.

    Args:
        password (str): The password.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create an access token.

    Args:
        data (dict): The data to encode in the token.
        expires_delta (timedelta | None, optional): The expiration delta. Defaults to None.

    Returns:
        str: The encoded access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
