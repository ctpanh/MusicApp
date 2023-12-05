from fastapi import Depends, HTTPException
from models.user import UserModel
from models.album import AlbumModel
from schemas.albumSchema import AlbumCreate
from database import getDatabase
from sqlalchemy.orm import Session


class AlbumController:
    @staticmethod
    # def createAlbum(Album: AlbumCreate, db: Session):
    #     newAlbum = AlbumModel(
    #         # user_id = request.user_id,
    #         title = Album.title,
    #         artist = Album.artist,
    #         audio_file_path = Album.audio_file_path,
    #         image_file_path = Album.image_file_path,
    #         album_id = Album.album_id,
    #         playlist_id = Album.playlist_id,
    #         release_date = Album.release_date,
    #         views = Album.views
    #     )
    #     db.add(newAlbum)
    #     db.commit()
    #     db.refresh(newAlbum)
    #     return newAlbum
    def createAlbum(album: AlbumCreate, db: Session = Depends(getDatabase)):
        new_Album = AlbumModel(
            title=album.title,
            release_date=album.release_date,
            artist=album.artist,
            genre_id=album.genre_id,
            image_file_path=album.image_file_path
        )
        db.add(new_Album)
        db.commit()
        db.refresh(new_Album)
        return new_Album
    
    
    def getAlbumById(AlbumId: int, db: Session = Depends(getDatabase)):
        return db.query(AlbumModel).filter(AlbumModel.id == AlbumId).first()

    def getAllAlbum(db: Session = Depends(getDatabase)):
        return db.query(AlbumModel).all()
    # def updateAlbum(AlbumId: int, Album: AlbumUpdate, db: Session):
    #     dbAlbumId = db.query(AlbumModel).filter(AlbumModel.id == AlbumId).first()

    #     if Album.name is not None:
    #         dbAlbumId.name = Album.name
    #     else:
    #         raise HTTPException(status_code=400, detail="Invalid name")

    #     db.commit()
    #     return {"msg": "Updated"}
    
    def deleteAlbum(AlbumId: int, db: Session):
        dbAlbumId = db.query(AlbumModel).filter(AlbumModel.id == AlbumId).first()
        db.delete(dbAlbumId)
        db.commit()
        return {"msg": "Deleted"}
    