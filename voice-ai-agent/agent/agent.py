import json
from agent.llm import extract_intent
from agent.tools import *
from memory.session_memory import *
from services.language_service import detect_language
from utils.latency import get_latency

def process_input(session_id, text):
    session = get_session(session_id)

    lang = detect_language(text)
    session["language"] = lang

    llm_output = extract_intent(text)

    try:
        data = json.loads(llm_output)
    except:
        return {"message": "Error understanding"}

    intent = data.get("intent")

    if intent == "book":
        slots = check_availability(data["doctor"], data["date"])

        if not slots:
            return {"message": "Slots unavailable"}

        result = book_appointment(data["doctor"], data["date"], slots[0])
        message = f"Booked at {slots[0]}"

    elif intent == "cancel":
        result = cancel_appointment(int(data.get("appointment_id", 1)))
        message = "Cancelled"

    elif intent == "reschedule":
        result = reschedule_appointment(int(data.get("appointment_id", 1)), data["time"])
        message = "Rescheduled"

    else:
        return {"message": "Unknown request"}

    if lang == "hi":
        message = "आपकी अपॉइंटमेंट पूरी हो गई है"
    elif lang == "ta":
        message = "உங்கள் நேரம் பதிவு செய்யப்பட்டது"

    update_session(session_id, session)

    return {
        "message": message,
        "data": result,
        "latency": get_latency()
    }