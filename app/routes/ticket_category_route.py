"""This module contains the routes for the ticket category."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import response_scheme, ticket_category, ticket_categories_user
from app.service import ticket_category as ticket_category_service
from app.service import ticket_categories_user as ticket_categories_user_service
from app.config import get_db
from app.service.authentication import auth

router = APIRouter()


@router.post("/create-category", dependencies=[Depends(auth.get_current_user)], response_model=response_scheme.Response)
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
    if category is None:
        raise HTTPException(
            status_code=400, detail="Category could not be created")
    response = response_scheme.Response(
        status=status.HTTP_200_OK, message="Category created")
    return response


@router.post("/assign-category", dependencies=[Depends(auth.get_current_user)], response_model=response_scheme.Response)
async def assign_category(category_in: ticket_categories_user.CreateTicketCategoryUser, db: Session = Depends(get_db)):
    """
    Assign a category to a user.
    """
    category = ticket_categories_user_service.assign_category(
        ticket=category_in, db=db)
    response = response_scheme.Response(
        status=status.HTTP_200_OK, message="Category assigned")
    return response


@router.get("/get-category/{user_id}", dependencies=[Depends(auth.get_current_user)], response_model=list[str])
async def get_category_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get the categories assigned to a user.
    """
    categories = ticket_categories_user_service.get_assigned_categories(
        user_id=user_id, db=db)
    return categories
