def add_task(todo):
    task = input("Enter the task to add: ")
    if task.strip():  # Avoid adding empty tasks
        todo.append(task)
        print(f'Task "{task}" added to the list.')
    else:
        print("Task cannot be empty.")

def remove_task(todo):
    if not todo:
        print("No tasks in the list.")
        return
    task = input("Enter the task to remove: ")
    if task in todo:
        todo.remove(task)
        print(f'Task "{task}" removed from the list.')
    else:
        print(f'Task "{task}" not found in the list.')

def view_tasks(todo):
    if not todo:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for i, task in enumerate(todo, 1):
            print(f"{i}. {task}")

def todo_list():
    todo = []
    while True:
        func_name = input("Enter function name (add_task, remove_task, view_tasks, quit): ").lower()
        if func_name == 'add_task':
            add_task(todo)
        elif func_name == 'remove_task':
            remove_task(todo)
        elif func_name == 'view_tasks':
            view_tasks(todo)
        elif func_name == 'quit':
            print("Exiting the todo list.")
            break
        else:
            print("Invalid option. Please choose add_task, remove_task, view_tasks, or quit.")

todo_list()
