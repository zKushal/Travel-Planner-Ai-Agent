from dotenv import load_dotenv
from agent.system_prompt import build_agent
from datetime import datetime, timezone
from db.connection import init_db, get_session

def main():
    init_db()
    agent = build_agent()

    print("\nWelcome to the Travel Planner AI Agent! You can ask me to create, view, or update your travel plans.\nType 'exit' or 'quit' to end the session.\n")


    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit", "cls", "goodbye", "bye"]:
            print("Thank you for using the Travel Planner AI Agent. Safe travels!")
            break

        if not user_input:
            print("Please enter a valid command or question.")
            continue

        result = agent.run_sync(user_input)
        print(f"\nAgent: {result.output}")

if __name__ == "__main__":
    load_dotenv()
    main()
