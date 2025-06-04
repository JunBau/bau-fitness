from sqlalchemy import Column, Integer, Float, String, CheckConstraint

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    goal = Column(String, nullable=False)  # "lose", "maintain", "gain"

    # Add check constraints
    __table_args__ = (
        CheckConstraint('age >= 13 AND age <= 120', name='check_age_range'),
        CheckConstraint('weight > 0 AND weight <= 500', name='check_weight_range'),
        CheckConstraint('height > 0 AND height <= 300', name='check_height_range'),
        CheckConstraint("goal IN ('lose', 'maintain', 'gain')", name='check_valid_goal'),
    ) 