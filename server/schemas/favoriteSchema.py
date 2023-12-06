from typing import Optional
from pydantic import BaseModel


class FavoriteAdd(BaseModel):
    user_id: int
    song_id: int