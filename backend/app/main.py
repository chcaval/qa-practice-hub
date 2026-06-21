from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import ai, users
from app.api.api import api_router


app = FastAPI(title="QA Practice API (MongoDB)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(ai.router)
app.include_router(api_router)