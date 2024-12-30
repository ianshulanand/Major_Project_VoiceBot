import time
from datetime import datetime

def set_reminder(reminder_time, message):
    # Convert string to datetime
    try:
        # Parse the reminder time string (assuming format HH:MM)
        reminder_time = datetime.strptime(reminder_time, '%H:%M')
        current_time = datetime.now()

        # Check if reminder time is in the future, otherwise add a day
        if reminder_time < current_time:
            reminder_time = reminder_time.replace(day=current_time.day + 1)

        print(f"Reminder set for {reminder_time.strftime('%H:%M')}. Message: {message}")
        return f"Reminder set for {reminder_time.strftime('%H:%M')} with message: {message}"

    except ValueError:
        print("Error: Invalid time format. Please provide the time in HH:MM format.")
        return "Error: Invalid time format. Please provide the time in HH:MM format."
