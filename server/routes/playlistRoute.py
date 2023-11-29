from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.playlistController import PlaylistController
from schemas.playlistSchema import PlaylistCreate
from models.playlist import PlaylistModel

router = APIRouter(
    tags=["Playlist"],
    responses={404: {"description": "Not found"}},
)

@router.post("/Playlist/create")
def createPlaylist(playlist: PlaylistCreate, db: Session = Depends(getDatabase)):
    return PlaylistController.createPlaylist(playlist=playlist, db=db)

@router.get("/Playlist/all")
def get_all_Playlist(db: Session = Depends(getDatabase)):
    return PlaylistController.getAllPlaylist(db=db)


@router.get("/Playlist/{playlistId}")
def get_Playlist_by_id(playlistId: int, db: Session = Depends(getDatabase)):
    return PlaylistController.getPlaylistById(playlistId=playlistId, db=db)


# @router.put("/Playlist/update/{PlaylistId}")
# def update_Playlist(PlaylistId: int, Playlist: UpdatePlaylist, db: Session = Depends(getDatabase)):
#     return PlaylistController.updatePlaylist(PlaylistId=PlaylistId, Playlist=Playlist, db=db)


@router.delete("/Playlist/delete/{playlistId}")
def delete_Playlist(
    playlistId: int, db: Session = Depends(getDatabase)
):
    
    return PlaylistController.deletePlaylist(playlistId=playlistId, db=db)