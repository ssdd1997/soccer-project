import json
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.config import Config
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse

import crud
import schemas
from database import SessionLocal, engine
from authlib.integrations.starlette_client import OAuth, OAuthError


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = Config('.env')
oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/clubs/", response_model=List[schemas.ClubWithPlayers])
def read_clubs(request: Request,skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    clubs = crud.get_clubs(db, skip=skip, limit=limit)
    return clubs


@app.get("/positions/", response_model=List[schemas.PositionWithPlayers])
def read_positions(request: Request,skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    positions = crud.get_positions(db, skip=skip, limit=limit)
    return positions


@app.get("/players/", response_model=List[schemas.PlayerWithClubAndPosition])
def read_players(request: Request, skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players


@app.get("/players/{id_player}", response_model=schemas.PlayerWithClubAndPosition)
def read_player(id_player: int, db: Session = Depends(get_db)):
    db_player = crud.get_player_by_id(db, id=id_player)
    if db_player is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_player


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
