"""This module contains the routes for the ticket category."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import ticket_category, ticket_categories_user, users
from app.service import ticket_category as ticket_category_service
from app.service import ticket_categories_user as ticket_categories_user_service
from app.config import get_db
from app.service.authentication import auth

router = APIRouter()


@router.post("/create-category", response_model=ticket_category.TicketCategoryInDBBase)
async def create_category(category_in: ticket_category.TicketCategoryCreate, current_user: users.UserInDBBase = Depends(auth.get_current_user), db: Session = Depends(get_db)):
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


@router.post("/assign-category", response_model=ticket_categories_user.TicketCategoryUserInDBBase)
async def assign_category(category_in: ticket_categories_user.CreateTicketCategoryUser, current_user: users.UserInDBBase = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Assign a category to a user.
    """
    category = ticket_categories_user_service.assign_category(
        ticket=category_in, db=db)
    return category


@router.get("/get-category/{user_id}", response_model=list[ticket_categories_user.TicketCategoryUserInDBBase])
async def get_category_by_user(current_user: users.UserInDBBase = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Get the categories assigned to a user.
    """
    categories = ticket_categories_user_service.get_assigned_categories(
        user_id=current_user.id, db=db)
    return categories
