from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return templates.TemplateResponse("index.html", {"request": {}})


posts = [
    {"id": 1, "title": "FastAPI: The New Python Web Framework", "url": "https://fastapi.tiangolo.com", "posted_at": "2024-09-12"},
    {"id": 2, "title": "HTMX and Tailwind CSS Integration", "url": "https://htmx.org", "posted_at": "2024-09-11"},
    {"id": 3, "title": "Django 4.0 Release Date Announced", "url": "https://www.djangoproject.com", "posted_at": "2024-09-10"},
    {"id": 4, "title": "Python 4.0 Features", "url": "https://www.python.org", "posted_at": "2024-09-09"},
    {"id": 5, "title": "Vue.js 4.0 Release Date Announced", "url": "https://vuejs.org", "posted_at": "2024-09-08"},
    {"id": 6, "title": "React 18 Alpha Release Date Announced", "url": "https://reactjs.org", "posted_at": "2024-09-07"},
    {"id": 7, "title": "Angular 13.0 Release Date Announced", "url": "https://angular.io", "posted_at": "2024-09-06"},
    {"id": 8, "title": "Svelte 4.0 Release Date Announced", "url": "https://svelte.dev", "posted_at": "2024-09-05"},
    {"id": 9, "title": "Ember.js 4.0 Release Date Announced", "url": "https://emberjs.com", "posted_at": "2024-09-04"},
    {"id": 10, "title": "Express.js 5.0 Release Date Announced", "url": "https://expressjs.com", "posted_at": "2024-09-03"},
]

@app.get("/posts", response_class=HTMLResponse)
async def read_posts():
    return templates.TemplateResponse("post.html", {"request": {}, "posts": posts})

