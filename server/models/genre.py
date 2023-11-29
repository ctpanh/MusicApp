from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# from models.album import AlbumModel 
from database import Base


# class GenreModel(Base):
#     __tablename__ = "Genres"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50))
#     # Relationship
#     albums = relationship("AlbumModel", back_populates="genre")

class GenreModel(Base):
    __tablename__ = "Genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    # Relationships
    albums = relationship("AlbumModel", back_populates="genre")