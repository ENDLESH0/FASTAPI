from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicacion Sencilla"
app.version = 0.0

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]
@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content="<h1> Mi aplicacion Sencilla </h1>")

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=['movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
        
@app.get("/movies/", tags=['movies'])
def get_movie_by_category(category: str):
    for movie in movies:
        if movie['category'] == category:
            return movie