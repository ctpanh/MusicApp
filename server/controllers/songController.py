from fastapi import Depends, HTTPException
from models.user import UserModel
from models.song import SongModel
from schemas.songSchema import SongCreate, SongUpdate
from database import getDatabase
from sqlalchemy.orm import Session


class SongController:
    @staticmethod
    # def createSong(song: SongCreate, db: Session):
    #     newSong = SongModel(
    #         # user_id = request.user_id,
    #         title = song.title,
    #         artist = song.artist,
    #         audio_file_path = song.audio_file_path,
    #         image_file_path = song.image_file_path,
    #         album_id = song.album_id,
    #         playlist_id = song.playlist_id,
    #         release_date = song.release_date,
    #         views = song.views
    #     )
    #     db.add(newSong)
    #     db.commit()
    #     db.refresh(newSong)
    #     return newSong
    def createSong(song: SongCreate, db: Session = Depends(getDatabase)):
        new_song = SongModel(
            title=song.title,
            artist=song.artist,
            audio_file_path=song.audio_file_path,
            image_file_path=song.image_file_path,
            album_id=song.album_id,
            playlist_id=song.playlist_id,
            release_date=song.release_date,
            views=song.views
        )
        db.add(new_song)
        db.commit()
        db.refresh(new_song)
        return new_song
    
    
    def getSongById(SongId: int, db: Session = Depends(getDatabase)):
        return db.query(SongModel).filter(SongModel.id == SongId).first()

    def getAllSong(db: Session = Depends(getDatabase)):
        return db.query(SongModel).all()
    def updateSong(SongId: int, Song: SongUpdate, db: Session):
        dbSongId = db.query(SongModel).filter(SongModel.id == SongId).first()

        if Song.views is not None:
            dbSongId.views = Song.views
        else:
            raise HTTPException(status_code=400, detail="Invalid views")

        db.commit()
        return {"msg": "Updated"}
    
    def deleteSong(songId: int, db: Session):
        dbSongId = db.query(SongModel).filter(SongModel.id == songId).first()
        db.delete(dbSongId)
        db.commit()
        return {"msg": "Deleted"}
    
        
    