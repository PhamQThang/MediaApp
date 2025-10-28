import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, UniqueConstraint
from app.models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Follower(Base):
    __tablename__ = "followers"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    follower_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    following_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    follower = relationship("User", foreign_keys=[follower_id], back_populates="following")
    following = relationship("User", foreign_keys=[following_id], back_populates="followers")


    __table_args__ = (UniqueConstraint("follower_id", "following_id", name="uq_follower_following"),)