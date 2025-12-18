from sqlalchemy import (
    Column, String, Integer, DateTime, ForeignKey, Text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(String, primary_key=True)
    timezone = Column(String, nullable=False)


class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(String, nullable=False)
    video_created_at = Column(DateTime(timezone=True), nullable=False)

    views_count = Column(Integer, nullable=False)
    likes_count = Column(Integer, nullable=False)
    comments_count = Column(Integer, nullable=False)
    reports_count = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    snapshots = relationship("VideoSnapshot", back_populates="video")


class VideoSnapshot(Base):
    __tablename__ = "video_snapshots"

    id = Column(Text, primary_key=True)
    video_id = Column(UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"))

    views_count = Column(Integer, nullable=False)
    likes_count = Column(Integer, nullable=False)
    comments_count = Column(Integer, nullable=False)
    reports_count = Column(Integer, nullable=False)

    delta_views_count = Column(Integer, nullable=False)
    delta_likes_count = Column(Integer, nullable=False)
    delta_comments_count = Column(Integer, nullable=False)
    delta_reports_count = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    video = relationship("Video", back_populates="snapshots")
