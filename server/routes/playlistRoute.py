from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.playlistController import PlaylistController
from schemas.playlistSchema import PlaylistCreate
from models.playlist import PlaylistModel

router = APIRouter(
    tags=["Playlist"],
    prefix="/playlist",
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
def createPlaylist(playlist: PlaylistCreate, db: Session = Depends(getDatabase)):
    return PlaylistController.createPlaylist(playlist=playlist, db=db)


@router.get("/all")
def get_all_Playlist(db: Session = Depends(getDatabase)):
    return PlaylistController.getAllPlaylist(db=db)


@router.get("/{playlistId}")
def get_Playlist_by_id(playlistId: int, db: Session = Depends(getDatabase)):
    return PlaylistController.getPlaylistById(playlistId=playlistId, db=db)


@router.get("/{playlistId}/songs")
def get_songs_by_playlist_id(playlistId: int, db: Session = Depends(getDatabase)):
    return PlaylistController.getSongsByPlaylistId(playlistId=playlistId, db=db)


# @router.put("/update/{PlaylistId}")
# def update_Playlist(PlaylistId: int, Playlist: UpdatePlaylist, db: Session = Depends(getDatabase)):
#     return PlaylistController.updatePlaylist(PlaylistId=PlaylistId, Playlist=Playlist, db=db)


@router.delete("/delete/{playlistId}")
def delete_Playlist(playlistId: int, db: Session = Depends(getDatabase)):
    return PlaylistController.deletePlaylist(playlistId=playlistId, db=db)
