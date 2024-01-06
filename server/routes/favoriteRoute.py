from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import getDatabase
from models.song import SongModel
from models.genre import GenreModel
from models.album import AlbumModel
from controllers.favoriteController import FavoriteController
from schemas.favoriteSchema import (
    FavoriteAdd,
)  # Adjust the import based on your actual model structure

router = APIRouter(
    tags=["Favorite"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add")
def addFavorite(favorite: FavoriteAdd, db: Session = Depends(getDatabase)):
    return FavoriteController.addFavorite(favorite=favorite, db=db)


@router.get("/all/{user_id}")
def get_all_favorite(user_id: int, db: Session = Depends(getDatabase)):
    return FavoriteController.getAllFavorite(user_id=user_id, db=db)


# @router.get("/{GenreId}")
# def get_Genre_by_id(GenreId: int, db: Session = Depends(getDatabase)):
#     return GenreController.getGenreById(GenreId=GenreId, db=db)


# # @router.put("/Genre/update/{GenreId}")
# # def update_Genre(GenreId: int, Genre: UpdateGenre, db: Session = Depends(getDatabase)):
# #     return GenreController.updateGenre(GenreId=GenreId, Genre=Genre, db=db)


@router.delete("/delete")
def delete_favorite(userId: int, songId: int, db: Session = Depends(getDatabase)):
    return FavoriteController.remove_favorite_song(
        user_id=userId, song_id=songId, db=db
    )
