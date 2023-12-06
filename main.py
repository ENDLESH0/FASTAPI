from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicacion Sencilla"
app.version = '0.0.1'

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
        

@app.post("/movies", tags=['movies'])
def create_movie(id: int = Body(),
                 title: str = Body,
                 overwiew: str = Body,
                 year:str = Body,
                 rating: float = Body,
                 category: str = Body):
    movies.append({
        'id':id,
        'title':title,
        'overwiew':overwiew,
        'rating':rating,
        'category':category
    })
    return movies

@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int,
                 title: str = Body(),
                 overwiew: str = Body(),
                 year:str = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] == title
            movie['overwiew'] == overwiew
            movie['year'] == year
            movie['rating'] == rating
            movie['category'] == category
            return movies
