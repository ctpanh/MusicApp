from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class GenreCreate(BaseModel):
    name: str

class GenreUpdate(BaseModel):
    name: str


