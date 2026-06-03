from datetime import datetime

class Task:
    def __init__(self, description, due_date_str, priority):
        self.description = description
        self.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        self.priority = priority

tasks = [
    Task("Task A", "2026-06-10", "High"),
    Task("Task B", "2026-05-01", "Medium"),
    Task("Task C", "2026-06-05", "Low")
]

tasks.sort(key=lambda t: t.due_date)

print("All Tasks:")
for task in tasks:
    print(f"{task.description} - Due: {task.due_date.strftime('%Y-%m-%d')} - Priority: {task.priority}")

now = datetime.now()
overdue_tasks = [task for task in tasks if task.due_date < now]

print("\nOverdue Tasks:")
for task in overdue_tasks:
    print(f"{task.description} - Overdue since: {task.due_date.strftime('%Y-%m-%d')}")