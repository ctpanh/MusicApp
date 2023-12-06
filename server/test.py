from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient
from datetime import datetime
from database import getDatabase

from models.song import SongModel

app = FastAPI()

# Your SQLAlchemy models and engine setup (similar to the previous example)

async def save_to_database(db: Session, item):
    try:
        new_song = SongModel(
            title=item['title'],
            artist=item['artist'],
            audio_file_path=item['audio_file_path'],
            image_file_path=item['image_file_path'],
            album_id=item['album_id'],
            playlist_id=item['playlist_id'],
            release_date=datetime.fromtimestamp(item['release_date']),
            views=item['views']
        )
        db.add(new_song)
        await db.commit()

        print(f"Song with ID {new_song.id} saved to the database.")
    except Exception as error:
        print('Error saving song to the database:', error)

@app.on_event("startup")
async def startup_event():
    # Your database setup (similar to the previous example)
    pass

@app.get("/zingmp3")
async def get_zingmp3_data(db: Session = Depends(getDatabase)):
    print("test")
    # Use the appropriate method to fetch data from the ZingMP3 API
    async with AsyncClient() as client:
        response = await client.get("https://example.com/zingmp3-api-endpoint")
        data = response.json()

    if data.get('data') and data['data'].get('items'):
        for item in data['data']['items']:
            print(item)
            await save_to_database(db, item)

    return {"message": "Data saved to the database."}
