"""This module contains the routes for the ticket category."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import ticket_category
from app.service import ticket_category as ticket_category_service
from app.config import get_db

router = APIRouter()


@router.post("/create-category", response_model=ticket_category.TicketCategoryInDBBase)
async def create_category(category_in: ticket_category.TicketCategoryCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    db_category = ticket_category_service.get_category_by_name(
        category_in.name, db)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    category = ticket_category_service.create_category(
        category=category_in, db=db)
    return category
