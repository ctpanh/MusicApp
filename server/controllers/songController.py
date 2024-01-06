from fastapi import Depends, HTTPException
from models.song import SongModel
from schemas.songSchema import SongCreate, SongUpdate
from database import getDatabase
from sqlalchemy.orm import Session


class SongController:
    def createSong(song: SongCreate, db: Session = Depends(getDatabase)):
        db_song = db.query(SongModel).filter(SongModel.code == song.code).first()
        if not db_song:
            db_song = SongModel(
                code=song.code,
                title=song.title,
                artist=song.artist,
                audio_file_path=song.audio_file_path,
                image_file_path=song.image_file_path,
                album_id=song.album_id,
                playlist_id=song.playlist_id,
                release_date=song.release_date,
                views=song.views,
            )
            db.add(db_song)
            db.commit()
            db.refresh(db_song)
        return db_song

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

    def updateViewSong(songId: int, db: Session):
        dbSongId = db.query(SongModel).filter(SongModel.id == songId).first()

        if dbSongId is not None:
            dbSongId.views = dbSongId.views + 1
            db.commit()
            return {"msg": "Updated"}
        else:
            raise HTTPException(status_code=400, detail="Invalid views")

    def deleteSong(songId: int, db: Session):
        dbSongId = db.query(SongModel).filter(SongModel.id == songId).first()
        db.delete(dbSongId)
        db.commit()
        return {"msg": "Deleted"}
