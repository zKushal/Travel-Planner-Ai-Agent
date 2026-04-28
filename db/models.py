from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TravelPlan(Base):

    __tablename__ = 'travelplanner'

    id= Column(Integer, primary_key = True)
    destination= Column(String)
    days= Column(Integer)
    start_date= Column(String)
    end_date= Column(String)
    status= Column(Boolean)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
)


    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'days': self.days,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status,
            'created_at': self.created_at
        }
    



   