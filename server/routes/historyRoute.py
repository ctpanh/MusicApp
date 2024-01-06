from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, aliased
from database import getDatabase
from models.song import SongModel
from models.album import AlbumModel
from models.history import HistoryModel
from schemas.historySchema import HistoryCreate
from controllers.historyController import HistoryController

router = APIRouter(
    tags=["History"],
    prefix="/history",
    responses={404: {"description": "Not found"}},
)


@router.post("/create_heard_songs")
def createHeardSong(history: HistoryCreate, db: Session = Depends(getDatabase)):
    return HistoryController.createHistory(history=history, db=db)


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
    if not recently_heard_songs:
        raise HTTPException(
            status_code=404, detail="No recently heard songs found for the user"
        )

    result = []

    # Iterate through ranked songs and create a dictionary for each
    for song in recently_heard_songs:
        album = db.query(AlbumModel).filter(AlbumModel.id == song.album_id).first()
        song_info = {
            "id": song.id,
            "album_id": song.album_id,
            "playlist_id": song.playlist_id,
            "title": song.title,
            "artist": song.artist,
            "audio_file_path": song.audio_file_path,
            "image_file_path": song.image_file_path,
            "release_date": song.release_date,
            "views": song.views,
            "albums_title": album.title,
        }
        result.append(song_info)

    return result
