from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

from sqlalchemy.orm import declarative_base

Base = declarative_base()

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
    



   