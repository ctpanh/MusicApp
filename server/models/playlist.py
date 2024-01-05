from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Text
import database
from database import Base
from sqlalchemy.orm import relationship


class PlaylistModel(Base):
    __tablename__ = "Playlists"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey("Users.id"))
