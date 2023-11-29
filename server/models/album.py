from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Text
import database
from database import Base
from sqlalchemy.orm import relationship
from models.genre import GenreModel 



# class AlbumModel(Base):
#     __tablename__ = "Albums"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100))
#     release_date = Column(DateTime)
#     artist =Column(String(100))
#     genre_id = Column(Integer, ForeignKey("Genres.id"))
#     # Relationships
#     songs = relationship("SongModel", back_populates="album")
#     genre = relationship("GenreModel", back_populates="albums")

class AlbumModel(Base):
    __tablename__ = "Albums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    release_date = Column(DateTime)
    artist = Column(String(100))
    genre_id = Column(Integer, ForeignKey("Genres.id"))

    # Relationships
    genre = relationship("GenreModel", back_populates="albums")
    songs = relationship("SongModel", back_populates="album")
    