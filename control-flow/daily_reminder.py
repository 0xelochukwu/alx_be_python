# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case statement based on priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. You can plan it according to your schedule.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. You can plan it according to your schedule.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task. Consider completing it soon.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority. Please check the input.")


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
