"""This module contains the exception handler for the FastAPI application."""
from fastapi import Request, status
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
