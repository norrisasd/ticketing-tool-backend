from typing import List, Tuple
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session
from app.model.ticket_category import TicketCategories
from app.model.tickets import Tickets
from app.schemas import tickets, response_scheme
from app.service import tickets as ticket_service
from app.config import get_db
from app.service.authentication import auth

router = APIRouter()


@router.post("/create-ticket", dependencies=[Depends(auth.get_current_user)], response_model=response_scheme.Response)
async def create_ticket(ticket_in: tickets.CreateTicket, db: Session = Depends(get_db)):
    """
    Create a new ticket.
    """
    ticket = ticket_service.create_ticket(ticket=ticket_in, db=db)
    response = response_scheme.Response(
        status=status.HTTP_201_CREATED, message="Ticket created")
    return response


@router.get("/get-tickets", response_model=list[tickets.TicketResponse])
async def get_tickets(db: Session = Depends(get_db)):
    """
    Get all tickets.
    """
    tickets = ticket_service.get_tickets(db)
    return tickets


@router.get("/get-ticket/{category}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_category(category: str, db: Session = Depends(get_db)):
    """
    Get tickets by category.
    """
    tickets = ticket_service.get_tickets_by_category(category=category, db=db)
    return tickets


@router.get("/get-unassigned-ticket/", response_model=list[tickets.TicketResponse])
async def get_unassigned_tickets(db: Session = Depends(get_db)):
    """
    Get unassigned tickets.
    """
    unassigned_tickets = ticket_service.get_unassigned_tickets(db)
    return unassigned_tickets


@router.get("/get-ticket/assigned_to/{id}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_assignee(id: int, db: Session = Depends(get_db)):
    """
    Get tickets by assignee.
    """
    assigned_tickets = ticket_service.get_tickets_by_assignee(
        assigned_to=id, db=db)
    return assigned_tickets


@router.get("/get-ticket/created_by/{id}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_creator(id: int, db: Session = Depends(get_db)):
    """
    Get tickets by creator.
    """
    created_tickets = ticket_service.get_tickets_by_creator(
        created_by=id, db=db)
    return created_tickets


@router.get("/get-ticket/{category}/status/{status}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_category_and_status(category: str, status: tickets.Status, db: Session = Depends(get_db)):
    """
    Get tickets by category and status.
    """
    tickets = ticket_service.get_tickets_by_category_and_status(
        category=category, status=status, db=db)
    return tickets


@router.get("/get-ticket/{category}/priority/{priority}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_category_and_priority(category: str, priority: tickets.Priority, db: Session = Depends(get_db)):
    """
    Get tickets by category and priority.
    """
    tickets = ticket_service.get_tickets_by_category_and_priority(
        category=category, priority=priority, db=db)
    return tickets


@router.get("/get-ticket/{category}/status/{status}/priority/{priority}", response_model=list[tickets.TicketResponse])
async def get_tickets_by_category_status_and_priority(category: str, status: tickets.Status, priority: tickets.Priority, db: Session = Depends(get_db)):
    """
    Get tickets by category, status and priority.
    """
    tickets = ticket_service.get_tickets_by_category_status_and_priority(
        category=category, status=status, priority=priority, db=db)
    return tickets


@router.put("/assign-ticket", response_model=tickets.TicketInDBBase)
async def assign_ticket(ticket_in: tickets.AssignTicket = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Assign a ticket to a user.
    """
    ticket = ticket_service.assign_ticket(ticket=ticket_in, db=db)
    return ticket


@router.put('/close-ticket', response_model=tickets.TicketInDBBase)
async def close_ticket(ticket_in: tickets.CloseTicket = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    """
    Close a ticket.
    """
    ticket = ticket_service.close_ticket(ticket=ticket_in, db=db)
    if ticket is None:
        raise HTTPException(
            status_code=400, detail="Ticket could not be closed")
    response = response_scheme.Response(
        status=status.HTTP_200_OK, message="Ticket closed")
    return ticket
