from fastapi import FastAPI
from app.routers import books, authors, genres
from app.auth import routes as auth_routes
from app.database import engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(genres.router)
app.include_router(auth_routes.router)