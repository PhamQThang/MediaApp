import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, String, Text, func
from app.models.base import Base
from sqlalchemy.orm import relationship


class Notification(Base):
    __tablename__ = "notifications"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recipient_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    type = Column(String(50), nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"), nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    recipient = relationship("User", foreign_keys=[recipient_id], back_populates="notifications")