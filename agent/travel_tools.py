from pydantic_ai import Agent
from typing import List, Dict
from datetime import datetime, timezone

from db.models import TravelPlan
from db.connection import get_session


def define_travel_tools(agent: Agent) -> None:

    @agent.tool_plain
    def create_plan(user: int, destination: str, days: int, start_date: datetime, end_date: datetime, status: bool = False) -> Dict: # means the plan is not yet confirmed
        """Creates a travel plan for the user and stores it in the database."""

        with get_session as session:
            new_plan = TravelPlan(
                user_id=user,
                destination=destination,
                days=days,
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat(),
                status=status
            )
            session.add(new_plan)
            session.commit()
            session.refresh(new_plan)
            return new_plan.to_dict()
        
    @agent.tool_plain
    def view_plans(user: int) -> List[Dict]: #means it will return a list of all the travel plans for the user based on the user id
        """Retrieves all travel plans for the user from the database."""

        with get_session as session:

            plans = session.get(TravelPlan).filter(TravelPlan.user_id == user).all()
            return [plan.to_dict() for plan in plans]
        

    @agent.tool_plain
    def update_plan(plan_id: int, destination: str = None, days: int = None, start_date: datetime = None, end_date: datetime = None, status: bool = None) -> Dict: # means it will update the travel plan based on the plan id
        """Updates an existing travel plan in the database."""

        with get_session as session:
            plan = session.get(TravelPlan).filter(TravelPlan.id == plan_id).first()
            if not plan:
                return {"error": "Plan not found"}

            if destination:
                plan.destination = destination
            if days:
                plan.days = days
            if start_date:
                plan.start_date = start_date.isoformat()
            if end_date:
                plan.end_date = end_date.isoformat()

            session.commit()
            session.refresh(plan)
            return plan.to_dict()
        
    @agent.tool_plain
    def delete_plan(plan_id: int) -> Dict: # means it will delete the travel plan based on the plan id
        """Deletes a travel plan from the database."""

        with get_session as session:
            plan = session.get(TravelPlan).filter(TravelPlan.id == plan_id).first()
            if not plan:
                return {"error": "Plan not found"}

            session.delete(plan)
            session.commit()
            return {"message": "Plan deleted successfully"}
        


