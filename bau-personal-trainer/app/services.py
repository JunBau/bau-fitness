from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from .models import UserSignup
from .database import User
from .exceptions import DuplicateEmailError, ValidationError, DatabaseError
from .constants import ErrorMessages

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserSignup) -> User:
        try:
            db_user = User(
                email=user_data.email,
                age=user_data.age,
                weight=user_data.weight,
                height=user_data.height,
                goal=user_data.goal
            )
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except IntegrityError as e:
            self.db.rollback()
            error_msg = str(e)
            if "UNIQUE constraint failed: users.email" in error_msg:
                raise DuplicateEmailError(ErrorMessages.EMAIL_EXISTS)
            elif "check_age_range" in error_msg:
                raise ValidationError(ErrorMessages.INVALID_AGE)
            elif "check_weight_range" in error_msg:
                raise ValidationError(ErrorMessages.INVALID_WEIGHT)
            elif "check_height_range" in error_msg:
                raise ValidationError(ErrorMessages.INVALID_HEIGHT)
            elif "check_valid_goal" in error_msg:
                raise ValidationError(ErrorMessages.INVALID_GOAL)
            raise ValidationError(str(e))
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(ErrorMessages.DATABASE_ERROR.format(str(e)))

    def get_all_users(self) -> List[User]:
        try:
            return self.db.query(User).all()
        except SQLAlchemyError as e:
            raise DatabaseError(ErrorMessages.DATABASE_ERROR.format(str(e)))
