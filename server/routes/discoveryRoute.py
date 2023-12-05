from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel
from models.genre import GenreModel
from models.album import AlbumModel  # Adjust the import based on your actual model structure

router = APIRouter(
    tags=["Discovery"],
    prefix="/discovery",
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
                'artist': song.artist,
                'audio_file_path': song.audio_file_path,
                'image_file_path': song.image_file_path,
                'album_id': song.album_id,
                'playlist_id': song.playlist_id,
                'release_date': song.release_date,
                'views': song.views
                # Add other fields as needed
            }
            for song in newest_songs
        ]

        return {'newest_songs': songs_list}

    except Exception as e:
        # Handle exceptions appropriately
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/albumByGenre/{genre_id}")
def list_albums_by_genre(genre_id: int, db: Session = Depends(getDatabase)):
    # Retrieve the genre by name
    genre = db.query(GenreModel).filter(GenreModel.id == genre_id).first()

    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    # Retrieve the songs for the given genre
    albums = db.query(AlbumModel).filter(AlbumModel.genre_id == genre.id).all()
    result = []

    # Iterate through albums and fetch associated songs
    for album in albums:
        # Retrieve songs for the current album
        songs = db.query(SongModel).filter(SongModel.album_id == album.id).all()

        # Create a dictionary for the current album with album name and songs
        album_info = {
            "album_name": album.title,
            "songs": [{"title": song.title, "artist": song.artist} for song in songs],
        }

        # Append the album info to the result list
        result.append(album_info)
    return result