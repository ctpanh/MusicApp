from fastapi import Depends, HTTPException
from models.user import UserModel
from models.favorite import FavoriteModel
from schemas.favoriteSchema import FavoriteAdd
from database import getDatabase
from sqlalchemy.orm import Session

from models.song import SongModel
from models.album import AlbumModel


class FavoriteController:
    @staticmethod
    def addFavorite(favorite: FavoriteAdd, db: Session):
        user = db.query(UserModel).filter(UserModel.id == favorite.user_id).first()
        song = db.query(SongModel).filter(SongModel.id == favorite.song_id).first()
        if not user or not song:
            raise HTTPException(status_code=404, detail="User or song not found")

        # Check if the song is already a favorite for the user
        if (
            db.query(FavoriteModel)
            .filter_by(user_id=favorite.user_id, song_id=favorite.song_id)
            .first()
        ):
            raise HTTPException(status_code=400, detail="Song is already a favorite")

        favorite_song = FavoriteModel(
            user_id=favorite.user_id, song_id=favorite.song_id
        )
        db.add(favorite_song)
        db.commit()

        return {"message": "Song added to favorites"}

    def getAllFavorite(user_id, db: Session = Depends(getDatabase)):
        favorite_songs = (
            db.query(SongModel)
            .join(FavoriteModel, FavoriteModel.song_id == SongModel.id)
            .filter(FavoriteModel.user_id == user_id)
            .all()
        )
        if not favorite_songs:
            raise HTTPException(
                status_code=404, detail="No favorite songs found for the user"
            )

        result = []

        for song in favorite_songs:
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

    def remove_favorite_song(
        user_id: int, song_id: int, db: Session = Depends(getDatabase)
    ):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        song = db.query(SongModel).filter(SongModel.id == song_id).first()

        if not user or not song:
            raise HTTPException(status_code=404, detail="User or song not found")

        favorite_song = (
            db.query(FavoriteModel).filter_by(user_id=user_id, song_id=song_id).first()
        )

        if not favorite_song:
            raise HTTPException(status_code=404, detail="Song is not a favorite")

        db.delete(favorite_song)
        db.commit()

        return {"message": "Song removed from favorites"}
