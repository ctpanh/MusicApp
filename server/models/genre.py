from sqlalchemy import Column, Integer, String
from database import Base


class GenreModel(Base):
    __tablename__ = "Genres"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    name = Column(String(50))
