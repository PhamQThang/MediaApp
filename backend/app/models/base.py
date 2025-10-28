from datetime import datetime
from sqlalchemy import Column, DateTime
from ..common.database import Base

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

__all__ = ['TimestampMixin', 'Base']