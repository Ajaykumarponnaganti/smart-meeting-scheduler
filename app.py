from datetime import datetime, timedelta
import calendar

WORKING_HOURS = (9, 17) 
PUBLIC_HOLIDAYS = ["2025-01-01", "2025-12-25"]  

schedule = {}

def is_working_day(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    if calendar.weekday(date_obj.year, date_obj.month, date_obj.day) >= 5:
        return False 
    if date_str in PUBLIC_HOLIDAYS:
        return False  
    return True

def get_available_slots(user, date_str):
    if not is_working_day(date_str):
        return []
    booked_slots = schedule.get(user, {}).get(date_str, [])
    all_slots = [(hour, hour + 1) for hour in range(WORKING_HOURS[0], WORKING_HOURS[1])]
    return [slot for slot in all_slots if slot not in booked_slots]

def schedule_meeting(user, date_str, start_hour, end_hour):
    if not is_working_day(date_str):
        return "Cannot schedule on weekends or public holidays."
    if start_hour < WORKING_HOURS[0] or end_hour > WORKING_HOURS[1] or start_hour >= end_hour:
        return "Invalid meeting time."
    
    schedule.setdefault(user, {}).setdefault(date_str, [])
    booked_slots = schedule[user][date_str]
    new_slot = (start_hour, end_hour)
    
    if any(start < new_slot[1] and end > new_slot[0] for start, end in booked_slots):
        return "Time slot is already booked."
    
    booked_slots.append(new_slot)
    return "Meeting scheduled successfully."

def view_meetings(user, date_str):
    return schedule.get(user, {}).get(date_str, []) or "No meetings scheduled."

# Example Usage
user = "Ajay"
date = "2025-03-18"
print(schedule_meeting(user, date, 10, 11))
print("Available slots:", get_available_slots(user, date))
print("Scheduled meetings:", view_meetings(user, date))
