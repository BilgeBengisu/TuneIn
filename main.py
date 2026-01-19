from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/songs", response_class=HTMLResponse)
async def songs_page(request: Request):
    return templates.TemplateResponse("songs.html", {"request": request})


@app.get("/song/{song_id}", response_class=HTMLResponse)
async def song_page(request: Request, song_id: int):
    # Song data - in a real app, this would come from a database
    songs = {
        1: {"title": "Song Title 1", "artist": "Artist Name"},
        2: {"title": "Song Title 2", "artist": "Artist Name"},
        3: {"title": "Song Title 3", "artist": "Artist Name"}
    }
    
    song = songs.get(song_id, {"title": "Unknown Song", "artist": "Unknown Artist"})
    
    return templates.TemplateResponse("song.html", {
        "request": request,
        "song_id": song_id,
        "song": song
    })
