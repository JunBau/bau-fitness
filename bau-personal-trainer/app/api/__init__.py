from fastapi import APIRouter
from .users.routes import router as users_router
from .workout_plans.routes import router as workout_plans_router

api_router = APIRouter()
api_router.include_router(users_router)
api_router.include_router(workout_plans_router) 