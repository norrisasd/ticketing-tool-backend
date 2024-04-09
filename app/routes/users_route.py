"""This module contains the user routes."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config import get_db
from app.service.authentication import auth, security
from app.model.users import User
from app.schemas import users
from app.service import users as user_service

router = APIRouter()


@router.post("/register", response_model=users.UserInDBBase)
async def register(user_in: users.CreateUser, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    db_user = auth.get_user(db, username=user_in.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    db_user = db.query(User).filter(User.email == user_in.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = user_service.register(user_in=user_in, db=db)
    return user


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> users.Token:
    """This function logs in a user and returns an access token."""
    user = auth.get_user(db, username=form_data.username)
    if not user or not security.pwd_context.verify(form_data.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return users.Token(access_token=access_token, token_type="bearer")


@router.get("/conversation/")
async def read_conversation(
    current_user: users.UserInDB = Depends(auth.get_current_user)
):
    """This function reads a conversation."""
    return {"message": "Hello World", "current_user": current_user}
