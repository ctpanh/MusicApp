from fastapi import Depends, HTTPException
from models.user import UserModel
from models.genre import GenreModel
from schemas.genreSchema import GenreCreate, GenreUpdate
from database import getDatabase
from sqlalchemy.orm import Session


class GenreController:
    @staticmethod
    def createGenre(genre: GenreCreate, db: Session):
        db_genre = db.query(GenreModel).filter(GenreModel.code == genre.code).first()
        if not db_genre:
            db_genre = GenreModel(
                code=genre.code,
                name=genre.name,
            )
            db.add(db_genre)
            db.commit()
            db.refresh(db_genre)
        return db_genre

    def getAllGenre(db: Session = Depends(getDatabase)):
        return db.query(GenreModel).all()

    def getGenreById(GenreId: int, db: Session = Depends(getDatabase)):
        return db.query(GenreModel).filter(GenreModel.id == GenreId).first()

    def updateGenre(GenreId: int, Genre: GenreUpdate, db: Session):
        dbGenreId = db.query(GenreModel).filter(GenreModel.id == GenreId).first()

        if Genre.name is not None:
            dbGenreId.name = Genre.name
        else:
            raise HTTPException(status_code=400, detail="Invalid name")

        db.commit()
        return {"msg": "Updated"}

    def deleteGenre(GenreId: int, db: Session):
        dbGenreId = db.query(GenreModel).filter(GenreModel.id == GenreId).first()
        db.delete(dbGenreId)
        db.commit()
        return {"msg": "Deleted"}
