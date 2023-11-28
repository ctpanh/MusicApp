from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel  # Adjust the import based on your actual model structure

router = APIRouter(
    tags=["Discovery"],
    responses={404: {"description": "Not found"}},
)

@router.get("/newest-songs")
def get_newest_songs(db: Session = Depends(getDatabase)):
    try:
        # Query the database to get the 12 newest songs
        newest_songs = (
            db.query(SongModel)
            .order_by(SongModel.release_date.desc())  # Order by release_date in descending order
            .limit(12)
            .all()
        )

        # Convert the SQLAlchemy objects to a list of dictionaries
        songs_list = [
            {
                'id': song.id,
                'title': song.title,
                'duration': song.duration,
                'audio_file_path': song.audio_file_path,
                'album_id': song.album_id,
                'artist_id': song.artist_id,
                'views': song.views
                # Add other fields as needed
            }
            for song in newest_songs
        ]

        return {'newest_songs': songs_list}

    except Exception as e:
        # Handle exceptions appropriately
        raise HTTPException(status_code=500, detail=str(e))
