from pydantic_ai import Agent
from typing import List, Dict
from datetime import datetime, timezone
from pydantic import BaseModel
from db.models import TravelPlan
from db.connection import get_session


def define_travel_tools(agent: Agent) -> None:

    @agent.tool_plain
    def create_plan(user_id: int, destination: str, days: int, plan_details:str, status: bool = False) -> Dict: # means the plan is not yet confirmed
        """Creates a travel plan for the user and stores it in the database."""

# This function takes the user ID, destination, number of days, plan details, and status as input. It creates a new travel plan in the database and returns the details of the created plan as a dictionary.
        with get_session() as session:
            new_plan = TravelPlan(
                user_id=user_id,
                destination=destination,
                days=days,
                plan_details = plan_details,
                status=status,
            )
            session.add(new_plan)
            session.commit()
            session.refresh(new_plan)
            return new_plan.to_dict()
        
    @agent.tool_plain
    def view_plans(user_id: int, limit: int = 1) -> List[Dict]:
        """Retrieves the most recent travel plans for the user (defaults to the latest 1 plan)."""

        with get_session() as session:
            plans = session.query(TravelPlan).filter(TravelPlan.user_id == user_id).order_by(TravelPlan.id.desc()).limit(limit).all()
            return [plan.to_dict() for plan in plans]
        

    @agent.tool_plain
    def update_plan(plan_id: int, 
                    destination: str = None, 
                    days: int = None,
                    plan_details:str = None, 
                    status: bool = None) -> Dict:
        
        """Updates an existing travel plan in the database."""

        with get_session() as session:
            plan = session.query(TravelPlan).filter(TravelPlan.id == plan_id).first()
            if not plan:
                return {"error": "Plan not found"}

            if destination:
                plan.destination = destination
            if days:
                plan.days = days
            if plan_details is not None:
                plan.plan_details = plan_details
            if status is not None:
                plan.status = status

            session.commit()
            session.refresh(plan)
            return plan.to_dict()
        
    @agent.tool_plain
    def delete_plan(plan_id: int) -> Dict: # means it will delete the travel plan based on the plan id
        """Deletes a travel plan from the database."""

        with get_session() as session:
            plan = session.query(TravelPlan).filter(TravelPlan.id == plan_id).first()
            if not plan:
                return {"error": "Plan not found"}

            session.delete(plan)
            session.commit()
            return {"message": "Plan deleted successfully"}
        


