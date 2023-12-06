from typing import List
from datetime import datetime
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import null
from database import Base, engine
from routes import userRoute, songRoute, albumRoute, genreRoute, playlistRoute, chartRoute, historyRoute, discoveryRoute, favoriteRoute
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient
from models.song import SongModel
from database import getDatabase
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship
from sqlalchemy.ext.asyncio import create_async_engine
from fastapi import FastAPI, HTTPException

from models.album import AlbumModel
from models.genre import GenreModel



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

class Album(BaseModel):
    album_title: str
    album_release_date: str
    album_artist: str
    album_genre: List[str]
    album_img_path: str

class Song(BaseModel):
    title: str
    artist: str
    audio_file_path: str
    image_file_path: str
    release_date: str  # Adjust the type if necessary
    views: int

class FullData(BaseModel):
    song: Song
    album: Album

@app.post("/save-data")
async def save_data(data: List[FullData], db: Session = Depends(getDatabase)):
    print("data", data)
    try:
        for full_data in data:
            song_data = full_data.song
            album_data = full_data.album

            for genre in album_data.album_genre:
                existing_genre = db.query(GenreModel).filter(GenreModel.name == genre).first()
                
                if not existing_genre:
                    # Genre already exists, skip adding
                    new_genre = GenreModel(name=genre)
                    db.add(new_genre)
                    db.commit()

                existing_album = db.query(AlbumModel).filter(AlbumModel.title == album_data.album_title).first()

                if not existing_album:
                    query_genre = db.query(GenreModel).filter(GenreModel.name == genre).first()
                    if query_genre:
                        album = AlbumModel(
                            title = album_data.album_title,
                            release_date = datetime.strptime(album_data.album_release_date, '%d/%m/%Y'),
                            artist = album_data.album_artist,
                            genre_id = query_genre.id,
                            image_file_path = album_data.album_img_path
                        )
                    db.add(album)
                    db.commit()
            # q_album = db.query(AlbumModel).filter(AlbumModel.title == album_data.album_title).first()
            # q_genre = db.query(GenreModel).filter(GenreModel.name == album_data.album_genre[0]).first()
            print(song_data)
            existing_song = db.query(SongModel).filter(SongModel.title == song_data.title).first()
            if not existing_song:
                song = SongModel(
                    title = song_data.title,
                    artist = song_data.artist,
                    audio_file_path = song_data.audio_file_path,
                    image_file_path = song_data.image_file_path,
                    album_id = None,
                    playlist_id = None,
                    release_date =datetime.fromisoformat(song_data.release_date[:-1]),
                    views = song_data.views
                )
                db.add(song)
                db.commit()
            
        # db.commit()
        return {"message": "Music tracks saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")
