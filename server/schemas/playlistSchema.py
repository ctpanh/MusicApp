from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlaylistCreate(BaseModel):
    name: str
    user_id: int

