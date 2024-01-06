from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel
from models.album import AlbumModel
from sqlalchemy.orm import aliased


router = APIRouter(
    tags=["Chart"],
    prefix="/chart",
    responses={404: {"description": "Not found"}},
)


@router.get("/rank")
def rank_songs_by_views(db: Session = Depends(getDatabase)):
    # Retrieve songs ranked by views in descending order
    ranked_songs = (
        db.query(
            SongModel.id,
            SongModel.album_id,
            SongModel.playlist_id,
            SongModel.title,
            SongModel.artist,
            SongModel.audio_file_path,
            SongModel.image_file_path,
            SongModel.release_date,
            SongModel.views,
        )
        .order_by(SongModel.views.desc())
        .limit(100)
        .all()
    )
    # Create a list to store the results
    result = []

    # Iterate through ranked songs and create a dictionary for each
    for song in ranked_songs:
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
