"""Main module for the FastAPI application"""
from fastapi import FastAPI
import uvicorn
from app.model import users
from app.routes import users_route
from .config import engine


app = FastAPI()

users.Base.metadata.create_all(bind=engine)

app.include_router(users_route.router)


def start() -> None:
    """Function Run the FastAPI server using Uvicorn"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
