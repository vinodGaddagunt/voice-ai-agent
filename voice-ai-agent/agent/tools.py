appointments = []

def check_availability(doctor, date):
    booked = [a["time"] for a in appointments if a["date"] == date]
    slots = ["10:00 AM", "2:00 PM", "4:00 PM"]
    return [s for s in slots if s not in booked]

def book_appointment(doctor, date, time):
    if time not in check_availability(doctor, date):
        return {"error": "Slot not available"}

    appointment = {
        "id": len(appointments) + 1,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    return appointment

def cancel_appointment(appointment_id):
    global appointments
    appointments = [a for a in appointments if a["id"] != appointment_id]
    return {"status": "cancelled"}

def reschedule_appointment(appointment_id, new_time):
    for a in appointments:
        if a["id"] == appointment_id:
            if new_time in check_availability(a["doctor"], a["date"]):
                a["time"] = new_time
                return {"status": "rescheduled"}
    return {"error": "failed"}