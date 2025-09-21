# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Provide Customized Reminder ---

# Check priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority level"

# Check if time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Always print the customized reminder
print("\nReminder:", reminder)
Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
Enter your task: Submit expenses
Priority (high/medium/low): medium
Is it time-bound? (yes/no): no

Reminder: 'Submit expenses' is a medium priority task

