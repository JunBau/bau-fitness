from app.database import Base, engine
from app.api.users.entities import User

# Import all models here
# from app.api.other_domain.entities import OtherModel

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine) 