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


@app.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get('/')
async def homepage(request: Request):
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        html = (
            f'<pre>{data}</pre>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse(url='/')


@app.get('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


@app.get("/clubs/", response_model=List[schemas.Club])
def read_clubs(request: Request,skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #user = request.session.get('user')
    #if user:
        clubs = crud.get_clubs(db, skip=skip, limit=limit)
        return clubs
    #return HTMLResponse('<a href="/login">login</a>')


@app.get("/positions/", response_model=List[schemas.Position])
def read_positions(request: Request,skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #user = request.session.get('user')
    #if user:
        positions = crud.get_positions(db, skip=skip, limit=limit)
        return positions
    #return HTMLResponse('<a href="/login">login</a>')


@app.get("/players/", response_model=List[schemas.Player])
def read_players(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #user = request.session.get('user')
    #if user:
        players = crud.get_players(db, skip=skip, limit=limit)
        return players
    #raise HTTPException(status_code=403, detail="User has not permission.")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
