from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.ticket_categories_user import TicketCategoriesUser
from app.model.ticket_category import TicketCategories
from app.schemas import ticket_categories_user


def assign_category(ticket: ticket_categories_user.CreateTicketCategoryUser, db: Session):
    """This function assigns a category to a user."""
    db_category_user = db.query(TicketCategoriesUser).filter(
        TicketCategoriesUser.user_id == ticket.user_id, TicketCategoriesUser.category_id == ticket.category_id).first()
    if db_category_user:
        raise HTTPException(
            status_code=400, detail="Category already assigned to the user.")
    db_category = TicketCategoriesUser(**ticket.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_assigned_categories(user_id: int, db: Session) -> list[str]:
    """This function returns the categories assigned to a user."""
    db_categories = db.query(TicketCategories).join(TicketCategoriesUser).filter(
        TicketCategoriesUser.user_id == user_id).all()
    categories: list[str] = [category.name for category in db_categories]
    return categories
