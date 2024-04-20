from sqlalchemy.orm import Session
from app.model.ticket_category import TicketCategories
from app.schemas import ticket_category


def create_category(category: ticket_category.TicketCategoryCreate, db: Session):
    """This function creates a new ticket category."""
    db_category = TicketCategories(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_name(name: str, db: Session):
    """This function retrieves a ticket category by name."""
    return db.query(TicketCategories).filter(TicketCategories.name == name).first()


def get_category_by_user(user_id: int, db: Session):
    """This function retrieves a ticket category by user id."""
    return db.query(TicketCategories).filter(TicketCategories.user_id == user_id).all()
