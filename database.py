from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product  # <-- Import Base from models

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Use the imported Base (with models attached)
Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
