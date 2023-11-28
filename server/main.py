from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import userRoute, songRoute, albumRoute, discoveryRoute


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(userRoute.router, prefix="/api")
app.include_router(discoveryRoute.router, prefix="/api")
app.include_router(songRoute.router, prefix="/api")
app.include_router(albumRoute.router, prefix="/api")


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
