"""Prompts for a task, its priority, and time sensitivity, then prints a customized reminder."""

task = input("Enter your task: ").strip()
priority = input(
    "Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

reminder = ""
match priority:
    case "high":
        reminder = f"REMINDER: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"REMINDER: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"REMINDER: '{task}' is a LOW priority task."
    case _:
        reminder = f"REMINDER: '{task}' has an unspecified priority."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)
