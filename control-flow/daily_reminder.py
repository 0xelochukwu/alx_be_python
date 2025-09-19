# daily_reminder.py

# single task
task = input("Enter your task: ")

# task's priority
priority = input("Priority (high/medium/low): ").lower()

# checking if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case statement based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". Consider completing it soon."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". You can plan it according to your schedule."


print()
print(reminder)


while True:
    another = input("\nWould you like to add another task? (yes/no): ").lower()
    if another == "yes":
        print("Great! Restart the program to input another task.")
        break
    elif another == "no":
        print("Have a productive day!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")
