from fastapi import Depends, HTTPException
from sqlalchemy import AliasedReturnsRows, func
from models.user import UserModel
from models.album import AlbumModel
from schemas.albumSchema import AlbumCreate
from database import getDatabase
from sqlalchemy.orm import Session

from models.song import SongModel
from sqlalchemy.orm import aliased


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
        db_album = db.query(AlbumModel).filter(AlbumModel.code == album.code).first()
        if not db_album:
            db_album = AlbumModel(
                code=album.code,
                title=album.title,
                release_date=album.release_date,
                artist=album.artist,
                genre_id=album.genre_id,
                image_file_path=album.image_file_path,
            )
            db.add(db_album)
            db.commit()
            db.refresh(db_album)
        return db_album

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

    def getFeatureAlbums(db: Session):
        album_alias = aliased(AlbumModel)

        # Subquery to get the top 3 albums by views
        top_album_subquery = (
            db.query(AlbumModel.id, func.sum(SongModel.views).label("total_views"))
            .join(SongModel, AlbumModel.id == SongModel.album_id)
            .group_by(AlbumModel.id)
            .order_by(func.sum(SongModel.views).desc())
            .limit(3)
            .subquery()
        )

        # Main query to get details of top 3 albums and their songs
        ranked_albums_and_songs = (
            db.query(
                AlbumModel.id,
                AlbumModel.title,
                SongModel.id.label("song_id"),
                SongModel.title.label("song_title"),
                SongModel.artist,
                SongModel.audio_file_path,
                SongModel.image_file_path,
                SongModel.release_date,
                SongModel.views,
            )
            .join(SongModel, AlbumModel.id == SongModel.album_id)
            .join(top_album_subquery, AlbumModel.id == top_album_subquery.c.id)
            .order_by(top_album_subquery.c.total_views.desc(), SongModel.views.desc())
            .all()
        )

        # Create a dictionary to store the results
        result = {}

        # Iterate through ranked albums and songs
        for (
            album_id,
            album_title,
            song_id,
            song_title,
            artist,
            audio_file_path,
            image_file_path,
            release_date,
            views,
        ) in ranked_albums_and_songs:
            # Add album information to the result dictionary if not already present
            if album_id not in result:
                result[album_id] = {
                    "album_id": album_id,
                    "album_title": album_title,
                    "total_views": 0,
                    "songs": [],
                }

            # Add song information to the album's list of songs
            song_info = {
                "song_id": song_id,
                "song_title": song_title,
                "artist": artist,
                "audio_file_path": audio_file_path,
                "image_file_path": image_file_path,
                "release_date": release_date,
                "views": views,
            }

            result[album_id]["songs"].append(song_info)
            result[album_id]["total_views"] += views

        # Convert the result dictionary to a list
        final_result = list(result.values())

        return final_result
