from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone
from db.connection import Base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# used to define the structure of the travel plan table in the database and to provide a method for converting the plan data into a dictionary format for easy manipulation and retrieval.
class TravelPlan(Base):

    __tablename__ = 'travelplanner'
# This model represents a travel plan created by a user. It includes details such as the destination, duration, start and end dates, and the status of the plan (confirmed or not).
    id= Column(Integer, primary_key = True)
    user_id= Column(Integer)
    destination= Column(String)
    days= Column(Integer)
    plan_details= Column(String)
    status= Column(Boolean)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
)


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'destination': self.destination,
            'days': self.days,
            'plan_details': self.plan_details,
            'status': self.status,
            'created_at': self.created_at
        }
    



   
