from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlbumCreate(BaseModel):
    title: str
    
    release_date: datetime
    artist: str
    genre_id: int

