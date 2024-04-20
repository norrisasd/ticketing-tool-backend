"""This module contains the service functions for the tickets."""
from sqlalchemy.orm import Session
from app.model.ticket_categories_user import TicketCategoriesUser
from app.model.tickets import Tickets
from app.schemas import tickets


def create_ticket(ticket: tickets.CreateTicket, db: Session):
    """This function creates a new ticket."""
    db_ticket = Tickets(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def assign_ticket(ticket: tickets.AssignTicket, db: Session):
    """This function assigns a ticket to a user."""
    db_ticket = db.query(Tickets).filter(Tickets.id == ticket.id).first()
    db_ticket.assigned_to_id = ticket.assigned_to
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
