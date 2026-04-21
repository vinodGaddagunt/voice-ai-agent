import json

def extract_intent(user_input):
    text = user_input.lower()

    if "book" in text:
        return {
            "intent": "book",
            "doctor": "cardiologist",
            "date": "tomorrow",
            "time": None
        }

    elif "cancel" in text:
        return {
            "intent": "cancel",
            "appointment_id": 1
        }

    elif "reschedule" in text:
        return {
            "intent": "reschedule",
            "appointment_id": 1,
            "time": "2:00 PM"
        }

    else:
        return {
            "intent": "unknown"
        }