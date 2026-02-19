import json
import os

FILE_NAME = "tasks.txt"

tasks = []  # Each task: {"task": "Buy milk" etc}


def load_tasks():
    """Load tasks from file if it exists."""
    global tasks

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []


def save_tasks():
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    """Add a new task."""
    task_name = input("Enter new task: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    tasks.append({"task": task_name, "done": False})
    print("Task added!")


def view_tasks():
    """Display all tasks."""
    if not tasks:
        print(" No tasks yet.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "1" if task["done"] else " "
        print(f"{i}. [{status}] {task['task']}")


def complete_task():
    """Mark a task as complete."""
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print(" Task marked as complete!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Delete a task."""
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f" Deleted: {removed['task']}")
        else:
            print(" Task does not exist.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display menu options."""
    print("\n====TO-DO LIST====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


# -------Main Program-----------
load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
        print(" Tasks saved. Goodbye!")
        break
    else:
        print(" Invalid choice!!. Please select 1-5.")
