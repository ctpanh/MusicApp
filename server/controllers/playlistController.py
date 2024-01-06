from fastapi import Depends
from models.playlist import PlaylistModel
from models.song import SongModel
from models.album import AlbumModel
from schemas.playlistSchema import PlaylistCreate
from database import getDatabase
from sqlalchemy.orm import Session


class PlaylistController:
    def createPlaylist(playlist: PlaylistCreate, db: Session = Depends(getDatabase)):
        db_playlist = (
            db.query(PlaylistModel).filter(PlaylistModel.code == playlist.code).first()
        )
        if not db_playlist:
            if playlist.user_id is not None:
                db_playlist = PlaylistModel(
                    code=playlist.code,
                    name=playlist.name,
                    user_id=playlist.user_id,
                    image_file_path=playlist.image_file_path,
                )
                db.add(db_playlist)
                db.commit()
                db.refresh(db_playlist)
            else:
                db_playlist = PlaylistModel(
                    code=playlist.code,
                    name=playlist.name,
                    image_file_path=playlist.image_file_path,
                )
                db.add(db_playlist)
                db.commit()
                db.refresh(db_playlist)
        return db_playlist

    def getPlaylistById(playlistId: int, db: Session = Depends(getDatabase)):
        return db.query(PlaylistModel).filter(PlaylistModel.id == playlistId).first()

    def getAllPlaylist(db: Session = Depends(getDatabase)):
        return db.query(PlaylistModel).all()

    def getSongsByPlaylistId(playlistId: int, db: Session = Depends(getDatabase)):
        songs = db.query(SongModel).filter(SongModel.playlist_id == playlistId).all()
        result = []
        for song in songs:
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
