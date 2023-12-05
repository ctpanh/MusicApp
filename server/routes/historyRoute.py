from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel
from models.history import HistoryModel
from schemas.historySchema import HistoryCreate
from controllers.historyController import HistoryController

router = APIRouter(
    tags=["History"],
    prefix="/history",
    responses={404: {"description": "Not found"}},
)

@router.get("/create_heard_songs/{user_id}")
def createHeardSong(history: HistoryCreate, db: Session = Depends(getDatabase)):
    return HistoryController.createGenre(history=history, db=db)

@router.get("/recently-heard-songs/{user_id}")
def get_recently_heard_songs(user_id: int, db: Session = Depends(getDatabase)):
    recently_heard_songs = (
        db.query(SongModel)
        .join(HistoryModel, HistoryModel.song_id == SongModel.id)
        .filter(HistoryModel.user_id == user_id)
        .order_by(HistoryModel.play_date.desc())
        .limit(10)
        .all()
    )

    # if not recently_heard_songs:
    #     raise HTTPException(status_code=404, detail="No recently heard songs found for the user")

    # # Return information about the recently heard songs
    # songs_info = [
    #     {
    #         "title": song.title,
    #         "artist": song.artist,
    #         "audio_file_path": song.audio_file_path,
    #         "image_file_path": song.image_file_path,
    #         "views": song.views,
    #         "last_played": history.play_date,
    #     }
    #     for song, history in recently_heard_songs
    # ]

    return recently_heard_songs
