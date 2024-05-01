"""This module contains the user routes."""
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config import get_db
from app.service.authentication import auth, security
from app.model.users import User
from app.schemas import users, response_scheme as json_response
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
) -> json_response.LoginResponse:
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

    response = json_response.LoginResponse(
        status=status.HTTP_200_OK, message="Login successful", access_token=access_token, token_type="bearer")
    response = JSONResponse(content=response.dict())
    response.set_cookie(key="auth.session", value=access_token)
    return response


@router.get("/users", response_model=list[users.UserInDBBase])
async def get_users(db: Session = Depends(get_db)):
    """
    Get all users.
    """
    all_users = user_service.get_users(db)
    return all_users
