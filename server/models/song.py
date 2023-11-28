from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Text
import database
from database import Base
from sqlalchemy.orm import relationship


# class SongModel(Base):
#     __tablename__ = "Songs"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100))
#     artist = Column(String(100))
#     audio_file_path = Column(String(255))
#     image_file_path = Column(String(255))
#     album_id = Column(Integer, ForeignKey("Albums.id"), nullable=True)
#     playlist_id = Column(Integer, ForeignKey("Playlists.id"), nullable=True)
#     release_date = Column(DateTime)
#     views = Column(Integer, default=0)
#     # Relationships
#     album = relationship("AlbumModel", back_populates="songs")

class SongModel(Base):
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    artist = Column(String(100))
    audio_file_path = Column(String(255))
    image_file_path = Column(String(255))
    album_id = Column(Integer, ForeignKey("Albums.id"), nullable=True)
    playlist_id = Column(Integer, ForeignKey("Playlists.id"), nullable=True)
    release_date = Column(DateTime)
    views = Column(Integer, default=0)

    # Define the relationship to AlbumModel after it's defined
    album = relationship("AlbumModel", back_populates="songs")