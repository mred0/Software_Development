tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def mark_task_completed():
    show_tasks()
    task_number = int(input("Enter task number to mark as completed: "))
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")

def menu():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_completed()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
