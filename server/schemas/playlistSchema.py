from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlaylistCreate(BaseModel):
    name: str
    code: str
    user_id: int
