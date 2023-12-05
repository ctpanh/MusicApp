from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.genreController import GenreController
from schemas.genreSchema import GenreCreate
from models.genre import GenreModel

router = APIRouter(
    tags=["Genre"],
    prefix="/genre",
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
def createGenre(genre: GenreCreate, db: Session = Depends(getDatabase)):
    return GenreController.createGenre(genre=genre, db=db)

@router.get("/all")
def get_all_Genre(db: Session = Depends(getDatabase)):
    return GenreController.getAllGenre(db=db)


@router.get("/{GenreId}")
def get_Genre_by_id(GenreId: int, db: Session = Depends(getDatabase)):
    return GenreController.getGenreById(GenreId=GenreId, db=db)


# @router.put("/Genre/update/{GenreId}")
# def update_Genre(GenreId: int, Genre: UpdateGenre, db: Session = Depends(getDatabase)):
#     return GenreController.updateGenre(GenreId=GenreId, Genre=Genre, db=db)


@router.delete("/delete/{GenreId}")
def delete_Genre(
    GenreId: int, db: Session = Depends(getDatabase)
):
    return GenreController.deleteGenre(GenreId=GenreId, db=db)