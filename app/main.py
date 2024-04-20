"""Main module for the FastAPI application"""
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import uvicorn
from app.model import users, tickets, ticket_category, ticket_categories_user
from app.routes import users_route, ticket_category_route, ticket_route
from app.utils import exception_handler
from .config import engine


app = FastAPI(
    # Add default path /api
    root_path="/api"
)

"""Exception handlers"""
app.add_exception_handler(RequestValidationError,
                          exception_handler.validation_exception_handler)
app.add_exception_handler(
    Exception, exception_handler.server_error_exception_handler)
app.add_exception_handler(RequestValidationError,
                          exception_handler.http_exception_handler)

# Create tables in the database
users.Base.metadata.create_all(bind=engine)
ticket_categories_user.Base.metadata.create_all(bind=engine)
tickets.Base.metadata.create_all(bind=engine)
ticket_category.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users_route.router)
app.include_router(ticket_category_route.router)
app.include_router(ticket_route.router)


def start() -> None:
    """Function Run the FastAPI server using Uvicorn"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000,
                reload=True, log_config="app/log_config.yaml")
