from agent.agent import process_input

def run_campaign():
    session = "campaign-user"

    print(process_input(session, "Reminder: appointment tomorrow"))
    print(process_input(session, "Reschedule it"))