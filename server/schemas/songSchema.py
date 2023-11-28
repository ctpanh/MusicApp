from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SongCreate(BaseModel):
    title: str
    artist: str
    audio_file_path: str
    image_file_path: str
    album_id: int
    playlist_id: int
    release_date: datetime
    views: int

