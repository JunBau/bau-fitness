from pydantic import BaseModel, EmailStr, Field
from typing import Literal

from .constants import ValidationRules, ErrorMessages

class UserSignup(BaseModel):
    email: EmailStr
    age: int = Field(
        ge=ValidationRules.MIN_AGE,
        le=ValidationRules.MAX_AGE,
        description=ErrorMessages.INVALID_AGE
    )
    weight: float = Field(
        gt=ValidationRules.MIN_WEIGHT,
        le=ValidationRules.MAX_WEIGHT,
        description=ErrorMessages.INVALID_WEIGHT
    )
    height: float = Field(
        gt=ValidationRules.MIN_HEIGHT,
        le=ValidationRules.MAX_HEIGHT,
        description=ErrorMessages.INVALID_HEIGHT
    )
    goal: Literal["lose", "maintain", "gain"]

class UserResponse(BaseModel):
    id: int
    email: str
    age: int
    weight: float
    height: float
    goal: str

    class Config:
        from_attributes = True  # This enables ORM model -> Pydantic model conversion
