"""This module contains the service functions for the tickets."""
from sqlalchemy.orm import Session, aliased
from sqlalchemy import or_
from fastapi import HTTPException
from app.model.ticket_categories_user import TicketCategoriesUser
from app.model.ticket_category import TicketCategories
from app.model.tickets import Tickets
from app.model.users import User
from app.model.ticket_closer import TicketCloser
from app.model.ticket_assigned import TicketAssignee
from app.schemas import tickets
from app.service import ticket_categories_user
from app.config import logger


def create_ticket(ticket: tickets.CreateTicket, db: Session):
    """This function creates a new ticket."""
    db_ticket = Tickets(**ticket.dict(exclude="assigned_to_id"))
    db.add(db_ticket)
    db.flush()

    if ticket.assigned_to_id is not None and ticket_categories_user.is_user_assigned_to_category(ticket.assigned_to_id, ticket.category_id, db) is False:
        raise HTTPException(
            status_code=400, detail="User is not assigned to the category.")
    db_ticket_assigned = TicketAssignee(
        ticket_id=db_ticket.id, assignee_id=ticket.assigned_to_id)
    db.add(db_ticket_assigned)
    db.flush()

    db_ticket_closed = TicketCloser(ticket_id=db_ticket.id)
    db.add(db_ticket_closed)

    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session):
    """This function returns all tickets."""
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_unassigned_tickets(db: Session):
    """This function returns all unassigned tickets."""
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id, isouter=True).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketAssignee.assignee_id == None).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_category(category: str, db: Session):
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketCategories.name == category).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_creator(created_by: int, db: Session):
    """
        This function returns all tickets created by a user.
    """
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(Tickets.created_by_id == created_by).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_category_and_status(category: str, status: str, db: Session):
    """
        This function returns all tickets by category and status.
    """
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketCategories.name == category, Tickets.status == status).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_category_and_priority(category: str, priority: str, db: Session):
    """
        This function returns all tickets by category and priority.
    """
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketCategories.name == category, Tickets.priority == priority).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_assignee(assigned_to: int, db: Session):
    """
        This function returns all tickets assigned to a user.
    """
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketAssignee.assignee_id == assigned_to).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def get_tickets_by_category_status_and_priority(category: str, status: str, priority: str, db: Session):
    """
        This function returns all tickets by category, status and priority.
    """
    creator = aliased(User)

    assignee = db.query(User.full_name).filter(
        User.id == TicketAssignee.assignee_id).as_scalar()
    closer = db.query(User.full_name).filter(
        User.id == TicketCloser.closed_by_id).as_scalar()

    db_tickets = db.query(
        Tickets, TicketCategories.name, creator.full_name, assignee, TicketCloser.closed_at, closer).join(TicketCategories, TicketCategories.id == Tickets.category_id).join(creator, creator.id == Tickets.created_by_id).join(TicketAssignee, TicketAssignee.ticket_id == Tickets.id).join(TicketCloser, TicketCloser.ticket_id == Tickets.id).filter(TicketCategories.name == category, Tickets.status == status, Tickets.priority == priority).order_by(Tickets.id).all()

    if db_tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")

    response: list[tickets.TicketResponse] = [
        tickets.TicketResponse(id=ticket.id, title=ticket.title, content=ticket.content, status=ticket.status, priority=ticket.priority, category=category, assigned_to=assignee, created_by=creator, created_at=ticket.created_at, closed_at=closed_at, closed_by=closer) for ticket, category, creator, assignee, closed_at, closer in db_tickets]
    return response


def assign_ticket(ticket: tickets.AssignTicket, db: Session):
    """This function assigns a ticket to a user."""
    db_ticket = db.query(TicketAssignee).filter(
        TicketAssignee.id == ticket.id).first()
    db_ticket.assignee_id = ticket.assigned_to
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def close_ticket(ticket: tickets.CloseTicket, db: Session):
    """This function closes a ticket."""
    db_ticket = db.query(Tickets).filter(Tickets.id == ticket.id).first()
    db_ticket.status = tickets.Status.CLOSED
    db_ticket.closed_by_id = ticket.closed_by
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
