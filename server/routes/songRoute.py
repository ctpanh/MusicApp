from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.songController import SongController
from schemas.songSchema import SongCreate, SongUpdate
from models.song import SongModel

router = APIRouter(
    tags=["Song"],
    responses={404: {"description": "Not found"}},
)

@router.post("/song/create")
def createSong(song: SongCreate, db: Session = Depends(getDatabase)):
    return SongController.createSong(song=song, db=db)

@router.get("/song/all")
def get_all_Song(db: Session = Depends(getDatabase)):
    return SongController.getAllSong(db=db)


@router.get("/song/{songId}")
def get_Song_by_id(songId: int, db: Session = Depends(getDatabase)):
    return SongController.getSongById(songId=songId, db=db)


@router.put("/Song/update/{SongId}")
def update_Song(SongId: int, Song: SongUpdate, db: Session = Depends(getDatabase)):
    return SongController.updateSong(SongId=SongId, Song=Song, db=db)


@router.delete("/song/delete/{songId}")
def delete_Song(
    songId: int, db: Session = Depends(getDatabase)
):
    
    return SongController.deleteSong(songId=songId, db=db)