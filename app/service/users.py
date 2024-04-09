"""This module contains the user service functions."""
from sqlalchemy.orm import Session
from app.model.users import User
from app.service.authentication import security
from app.schemas import users


def register(user_in: users.CreateUser, db: Session):
    """This function registers a new user."""
    hashed_password = security.get_password_hash(user_in.password)
    user = User(**user_in.dict(exclude="password"),
                hash_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
