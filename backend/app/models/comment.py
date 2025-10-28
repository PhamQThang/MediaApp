import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Text, func
from app.models.base import Base
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comments"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    content = Column(Text, nullable=False)
    parent_comment_id = Column(UUID(as_uuid=True), ForeignKey("comments.id", ondelete="CASCADE"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")
    replies = relationship("Comment", cascade="all, delete-orphan")
    likes = relationship("Like", back_populates="comment", cascade="all, delete-orphan")