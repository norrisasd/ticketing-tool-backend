from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import tickets
from app.service import tickets as ticket_service
from app.config import get_db

router = APIRouter()


@router.post("/create-ticket", response_model=tickets.TicketInDBBase)
async def create_ticket(ticket_in: tickets.CreateTicket, db: Session = Depends(get_db)):
    """
    Create a new ticket.
    """
    ticket = ticket_service.create_ticket(ticket=ticket_in, db=db)
    return ticket
