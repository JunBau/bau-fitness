from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import get_db
from .models import UserSignup, UserResponse
from .services import UserService
from .constants import ErrorMessages

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)

@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_all_users()

@router.post("/foo")
def foo():
    return {"message": "Bar"}