"""This module contains the exception handler for the FastAPI application."""
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config import logger


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Validation error handler"""
    if status.HTTP_422_UNPROCESSABLE_ENTITY:
        logger.error(f"Status code: {status.HTTP_422_UNPROCESSABLE_ENTITY}")
        logger.error(f"Validation error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"detail": "There is something wrong with the content/input", "body": exc.body}),
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    """HTTP error handler"""
    if status.HTTP_400_BAD_REQUEST:
        logger.error(f"Status code: {status.HTTP_400_BAD_REQUEST}")
        logger.error(f"HTTP error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Bad Request", "body": exc.args[0]}),
    )


async def server_error_exception_handler(request: Request, exc: Exception):
    """Server error handler"""
    if status.HTTP_500_INTERNAL_SERVER_ERROR:
        logger.error(f"Status code: {status.HTTP_500_INTERNAL_SERVER_ERROR}")
        logger.error(f"Server error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {"detail": "Internal Server Error", "body": exc}),
    )
