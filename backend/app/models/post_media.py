import uuid
from sqlalchemy import UUID, Column, ForeignKey, String, Text
from app.models.base import Base
from sqlalchemy.orm import relationship


class PostMedia(Base):
    __tablename__ = "post_media"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True)
    media_url = Column(Text, nullable=False)
    media_type = Column(String(20), nullable=False)


    post = relationship("Post", back_populates="media")