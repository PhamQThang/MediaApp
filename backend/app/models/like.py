import uuid
from sqlalchemy import UUID, CheckConstraint, Column, DateTime, ForeignKey, func
from app.models.base import Base
from sqlalchemy.orm import relationship


class Like(Base):
    __tablename__ = "likes"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"), nullable=True, index=True)
    comment_id = Column(UUID(as_uuid=True), ForeignKey("comments.id", ondelete="CASCADE"), nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")


    __table_args__ = (
    CheckConstraint("(post_id IS NOT NULL) OR (comment_id IS NOT NULL)", name="like_post_or_comment_ck"),
    )