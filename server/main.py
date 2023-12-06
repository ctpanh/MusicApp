from typing import List
import datetime
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

@app.post("/save-data")
async def save_data(data: dict, db: Session = Depends(getDatabase)):
    try:
        # Save the data to the database
        print(data)
        saved_song = save_data(db, data)
        return {"message": "Music track saved successfully", "saved_song_id": saved_song.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")

    

@app.post("/save-data")
async def save_data(tracks: List[dict], db: Session = Depends(getDatabase)):
    try:
        for track in tracks:
            # Save each track to the database
            saved_track = SongModel(
                title=track.get('title'),
                artist=track.get('artistsNames'),
                # Add other fields accordingly
            )
            db.add(saved_track)

        db.commit()
        return {"message": "Music tracks saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")