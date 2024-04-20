from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.ticket_categories_user import TicketCategoriesUser
from app.schemas import ticket_categories_user


def assign_category(ticket: ticket_categories_user.CreateTicketCategoryUser, db: Session):
    """This function assigns a category to a user."""
    try:
        db_category_user = db.query(TicketCategoriesUser).filter(
            TicketCategoriesUser.user_id == ticket.user_id, TicketCategoriesUser.category_id == ticket.category_id).first()
        if db_category_user:
            raise HTTPException(
                status_code=400, detail="Category already assigned to the user.")
        db_category = TicketCategoriesUser(**ticket.dict())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
    except:
        raise HTTPException(
            status_code=400, detail="There was an error assigning the category.")
    return db_category


def get_assigned_categories(user_id: int, db: Session):
    """This function returns the categories assigned to a user."""
    return db.query(TicketCategoriesUser).filter(TicketCategoriesUser.user_id == user_id).all()
