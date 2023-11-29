from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel

router = APIRouter(
    tags=["Chart"],
    responses={404: {"description": "Not found"}},
)

@router.get("/chart/rank")
def rank_songs_by_views(db: Session = Depends(getDatabase)):
    # Retrieve songs ranked by views in descending order
    ranked_songs = db.query(SongModel).order_by(SongModel.views.desc()).all()

    # Create a list to store the results
    # result = []

    # # Iterate through ranked songs and create a dictionary for each
    # for song in ranked_songs:
    #     song_info = {
    #         "title": song.title,
    #         "artist": song.artist,
    #         "views": song.views,
    #     }
    #     result.append(song_info)

    return ranked_songs
