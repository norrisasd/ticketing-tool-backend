from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimeStamp:
    """this class creates a timestamp mixin."""
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now(), nullable=False)
