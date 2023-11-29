from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HistoryCreate(BaseModel):
    user_id: int
    song_id: int
    play_date: datetime

