from fastapi import FastAPI
from app.api import api_router
from app.database_init import init_db

app = FastAPI(title="Fitness App API")

# Initialize database
init_db()

app.include_router(api_router)