from sqlalchemy.orm import Session
from app.model.tickets import Tickets
from app.schemas import tickets


def create_ticket(ticket: tickets.CreateTicket, db: Session):
    """This function creates a new ticket."""
    db_ticket = Tickets(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
