from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import tickets
from app.service import tickets as ticket_service
from app.config import get_db
from app.service.authentication import auth

router = APIRouter()


@router.post("/create-ticket", response_model=tickets.TicketInDBBase)
async def create_ticket(ticket_in: tickets.CreateTicket = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Create a new ticket.
    """
    ticket = ticket_service.create_ticket(ticket=ticket_in, db=db)
    return ticket


@router.post("/assign-ticket", response_model=tickets.TicketInDBBase)
async def assign_ticket(ticket_in: tickets.AssignTicket = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Assign a ticket to a user.
    """
    ticket = ticket_service.assign_ticket(ticket=ticket_in, db=db)
    return ticket
