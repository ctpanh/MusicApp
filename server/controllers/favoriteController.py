from fastapi import Depends, HTTPException
from models.user import UserModel
from models.favorite import FavoriteModel
from schemas.favoriteSchema import FavoriteAdd
from database import getDatabase
from sqlalchemy.orm import Session

from models.song import SongModel


class FavoriteController:
    @staticmethod
    def addFavorite(favorite: FavoriteAdd, db: Session):
        user = db.query(UserModel).filter(UserModel.id == favorite.user_id).first()
        song = db.query(SongModel).filter(SongModel.id == favorite.song_id).first()
        if not user or not song:
            raise HTTPException(status_code=404, detail="User or song not found")

        # Check if the song is already a favorite for the user
        if db.query(FavoriteModel).filter_by(user_id=favorite.user_id, song_id=favorite.song_id).first():
            raise HTTPException(status_code=400, detail="Song is already a favorite")
        
        favorite_song = FavoriteModel(user_id=favorite.user_id, song_id=favorite.song_id)
        db.add(favorite_song)
        db.commit()

        return {"message": "Song added to favorites"}
        
    def getAllFavorite(user_id, db: Session = Depends(getDatabase)):
        return db.query(FavoriteModel).filter(UserModel.id==user_id).all()


    def remove_favorite_song(user_id: int, song_id: int, db: Session = Depends(getDatabase)):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        song = db.query(SongModel).filter(SongModel.id == song_id).first()

        if not user or not song:
            raise HTTPException(status_code=404, detail="User or song not found")

        favorite_song = db.query(FavoriteModel).filter_by(user_id=user_id, song_id=song_id).first()

        if not favorite_song:
            raise HTTPException(status_code=404, detail="Song is not a favorite")

        db.delete(favorite_song)
        db.commit()

        return {"message": "Song removed from favorites"}
    