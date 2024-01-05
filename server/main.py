import json
from datetime import datetime
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import (
    userRoute,
    songRoute,
    albumRoute,
    genreRoute,
    playlistRoute,
    chartRoute,
    historyRoute,
    discoveryRoute,
    favoriteRoute,
)
from controllers.playlistController import PlaylistController
from controllers.genreController import GenreController
from controllers.albumController import AlbumController
from controllers.songController import SongController
from schemas.playlistSchema import PlaylistCreate
from schemas.genreSchema import GenreCreate
from schemas.albumSchema import AlbumCreate
from schemas.songSchema import SongCreate
from sqlalchemy.orm import Session
from database import getDatabase
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException

from models.genre import GenreModel
from models.playlist import PlaylistModel


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(userRoute.router, prefix="/api")
app.include_router(discoveryRoute.router, prefix="/api")
app.include_router(songRoute.router, prefix="/api")
app.include_router(albumRoute.router, prefix="/api")
app.include_router(genreRoute.router, prefix="/api")
app.include_router(playlistRoute.router, prefix="/api")
app.include_router(chartRoute.router, prefix="/api")
app.include_router(historyRoute.router, prefix="/api")
app.include_router(favoriteRoute.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "sentry-trace", "baggage"],
)


@app.get("/api/ping")
def ping():
    return "pong"


@app.get("/api/data")
async def save_data(db: Session = Depends(getDatabase)):
    try:
        file_path = "data/playlists.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        for item in data:
            playlist = PlaylistCreate(
                name=item.get("name"),
                code=item.get("code"),
                image_file_path=item.get("image_file_path"),
            )
            PlaylistController.createPlaylist(playlist=playlist, db=db)

        file_path = "data/genres.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        for item in data:
            genre = GenreCreate(
                name=item.get("name"),
                code=item.get("id"),
            )
            GenreController.createGenre(genre=genre, db=db)

        file_path = "data/songs.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        for item in data:
            date_object = datetime.strptime(
                item.get("album").get("release_date"), "%d/%m/%Y"
            )
            formatted_date = date_object.strftime("%Y-%m-%dT%H:%M:%S")

            for genre in item.get("album").get("genre"):
                db_genre = db.query(GenreModel).filter(GenreModel.code == genre).first()
                if db_genre:
                    album = AlbumCreate(
                        title=item.get("album").get("title"),
                        code=item.get("album").get("code"),
                        image_file_path=item.get("album").get("image_file_path"),
                        release_date=formatted_date,
                        artist=item.get("album").get("artist"),
                        genre_id=db_genre.id,
                    )
                    album = AlbumController.createAlbum(album=album, db=db)
                    break

            for playlist in item.get("playlist_id"):
                db_playlist = (
                    db.query(PlaylistModel)
                    .filter(PlaylistModel.code == playlist)
                    .first()
                )
                if db_playlist:
                    song = SongCreate(
                        code=item.get("code"),
                        title=item.get("title"),
                        artist=item.get("artist"),
                        audio_file_path=item.get("audio_file_path"),
                        image_file_path=item.get("image_file_path"),
                        album_id=album.id,
                        playlist_id=db_playlist.id,
                        release_date=item.get("release_date"),
                        views=0,
                    )
                    SongController.createSong(song=song, db=db)
                    break

        return {"message": "Data saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")
