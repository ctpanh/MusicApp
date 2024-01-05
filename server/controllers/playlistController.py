from fastapi import Depends, HTTPException
from models.user import UserModel
from models.playlist import PlaylistModel
from schemas.playlistSchema import PlaylistCreate
from database import getDatabase
from sqlalchemy.orm import Session


class PlaylistController:
    @staticmethod
    # def createPlaylist(Playlist: PlaylistCreate, db: Session):
    #     newPlaylist = PlaylistModel(
    #         # user_id = request.user_id,
    #         title = Playlist.title,
    #         artist = Playlist.artist,
    #         audio_file_path = Playlist.audio_file_path,
    #         image_file_path = Playlist.image_file_path,
    #         album_id = Playlist.album_id,
    #         playlist_id = Playlist.playlist_id,
    #         release_date = Playlist.release_date,
    #         views = Playlist.views
    #     )
    #     db.add(newPlaylist)
    #     db.commit()
    #     db.refresh(newPlaylist)
    #     return newPlaylist
    def createPlaylist(playlist: PlaylistCreate, db: Session = Depends(getDatabase)):
        db_playlist = (
            db.query(PlaylistModel).filter(PlaylistModel.code == playlist.code).first()
        )
        if not db_playlist:
            db_playlist = PlaylistModel(
                code=playlist.code,
                name=playlist.name,
                user_id=playlist.user_id,
            )
            db.add(db_playlist)
            db.commit()
            db.refresh(db_playlist)
        return db_playlist

    def getPlaylistById(playlistId: int, db: Session = Depends(getDatabase)):
        return db.query(PlaylistModel).filter(PlaylistModel.id == playlistId).first()

    def getAllPlaylist(db: Session = Depends(getDatabase)):
        return db.query(PlaylistModel).all()

    # def updatePlaylist(PlaylistId: int, Playlist: PlaylistUpdate, db: Session):
    #     dbPlaylistId = db.query(PlaylistModel).filter(PlaylistModel.id == PlaylistId).first()

    #     if Playlist.name is not None:
    #         dbPlaylistId.name = Playlist.name
    #     else:
    #         raise HTTPException(status_code=400, detail="Invalid name")

    #     db.commit()
    #     return {"msg": "Updated"}

    def deletePlaylist(playlistId: int, db: Session):
        dbPlaylistId = (
            db.query(PlaylistModel).filter(PlaylistModel.id == playlistId).first()
        )
        db.delete(dbPlaylistId)
        db.commit()
        return {"msg": "Deleted"}
