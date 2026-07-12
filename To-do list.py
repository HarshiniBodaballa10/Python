tasks = []
def add_task(task):
    tasks.append(task)
    print("Task is added.")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task is removed.")
    else:
        print("Task not found.")
def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
while True:
    choice = input("Enter the choice ('add', 'remove', 'view', 'quit'): ").strip().lower()
    if choice == 'add':
        task = input("Enter the task to add: ").strip()
        add_task(task)
    elif choice == 'remove':
        task = input("Enter the task to remove: ").strip()  # Fix: Ensure task is passed to remove_task()
        remove_task(task)
    elif choice == 'view':
        view_task()
    elif choice == 'quit':
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
