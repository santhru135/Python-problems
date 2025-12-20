def add_task(todo):
    task = input("Enter the task to add: ")
    if task.strip():
        todo.append(task)
        print(f'Task "{task}" added to the list.')
    else:
        print("Task cannot be empty.")

def remove_task(todo):
    if not todo:
        print("No tasks in the list.")
        return
    task = int(input("Enter the task to remove: "))
    if task <= len(todo) and task > 0:
        del todo[task-1]
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
        func_name = input(" 1.Add Task\n 2.Remove Task\n 3.View Tasks\n 4.Quit.\n Enter function name: ").lower()
        if func_name == '1' or func_name == 'Add Task'.lower():
            add_task(todo)
        elif func_name == '2' or func_name == 'Remove Task'.lower():
            remove_task(todo)
        elif func_name == '3' or func_name == 'View Tasks'.lower():
            view_tasks(todo)
        elif func_name == '4' or func_name == 'Quit'.lower():
            print("Exiting the todo list.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

todo_list()