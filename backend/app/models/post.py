from sqlalchemy import  Column, DateTime, Integer, String, ForeignKey, Enum as SQLEnum, Text, func
from sqlalchemy.orm import relationship
import enum
from app.models.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class Post(Base):
    __tablename__ = "posts"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    content = Column(Text)
    visibility = Column(String(20), nullable=False, default="public")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


    user = relationship("User", back_populates="posts")
    media = relationship("PostMedia", back_populates="post", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    likes = relationship("Like", back_populates="post", cascade="all, delete-orphan")
    hashtags = relationship("PostHashtag", back_populates="post", cascade="all, delete-orphan")