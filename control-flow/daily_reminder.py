#daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task. Try to complete it soon."
    case "low":
        message = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = "Invalid priority level. Please enter high, medium, or low."

if priority in ["high", "medium", "low"] and time_bound == "yes":
    message += " that requires immediate attention today!"

print("Reminder:", message)
