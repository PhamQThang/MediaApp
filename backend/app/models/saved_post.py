import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Text, UniqueConstraint, func
from app.models.base import Base
from sqlalchemy.orm import relationship


class SavedPost(Base):
    __tablename__ = "saved_posts"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    user = relationship("User", back_populates="saved_posts")
    post = relationship("Post")


    __table_args__ = (UniqueConstraint("user_id", "post_id", name="uq_user_saved_post"),)