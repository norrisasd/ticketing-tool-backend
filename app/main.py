"""Main module for the FastAPI application"""
from fastapi import FastAPI
import uvicorn
from app.model import users
from .config import engine

from app.routes import users_route

app = FastAPI()

users.Base.metadata.create_all(bind=engine)


@app.get("/")
async def main_route():
    """Function to return a simple message"""
    return {"message": "Running FastAPI Python"}

app.include_router(users_route.router)


def start() -> None:
    """Function Run the FastAPI server using Uvicorn"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
