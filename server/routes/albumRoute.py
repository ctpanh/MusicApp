from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.albumController import AlbumController
from schemas.albumSchema import AlbumCreate
from models.album import AlbumModel
from models.genre import GenreModel  # Import Genre here


router = APIRouter(
    tags=["Album"],
    responses={404: {"description": "Not found"}},
)

@router.post("/Album/create")
def createAlbum(album: AlbumCreate, db: Session = Depends(getDatabase)):
    return AlbumController.createAlbum(album=album, db=db)

@router.get("/Album/all")
def get_all_Album(db: Session = Depends(getDatabase)):
    return AlbumController.getAllAlbum(db=db)


@router.get("/Album/{AlbumId}")
def get_Album_by_id(AlbumId: int, db: Session = Depends(getDatabase)):
    return AlbumController.getAlbumById(AlbumId=AlbumId, db=db)


# @router.put("/Album/update/{AlbumId}")
# def update_Album(AlbumId: int, Album: UpdateAlbum, db: Session = Depends(getDatabase)):
#     return AlbumController.updateAlbum(AlbumId=AlbumId, Album=Album, db=db)


@router.delete("/Album/delete/{AlbumId}")
def delete_Album(
    AlbumId: int, db: Session = Depends(getDatabase)
):
    return AlbumController.deleteAlbum(AlbumId=AlbumId, db=db)