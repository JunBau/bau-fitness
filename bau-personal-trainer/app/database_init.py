from app.database import Base, engine
from app.api.users.entities import User
from app.api.workout_plans.entities import WorkoutPlan, Exercise, ExerciseProgress

# Import all models here
# from app.api.other_domain.entities import OtherModel

def init_db():
    # Drop all tables to ensure clean state with new schema
    Base.metadata.drop_all(bind=engine)
    # Create all tables
    Base.metadata.create_all(bind=engine) 