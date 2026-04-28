from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


DATABASE_URL="postgresql://postgres:k4sh@L1014localhost:5432/TravelPlannerDB"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )

Base = declarative_base()

# this function will create the database tables based on the models defined in db/models.py
def init_db():
    from db.models import TravelPlan
    Base.metadata.create_all(bind=engine)

@contextmanager
# this function will provide a session to interact with the database and will ensure that the session is closed after use
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
