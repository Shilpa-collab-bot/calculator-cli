# Empty list to store tasks
tassks=[]
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        tassks.append(task)
        print(f'Task "{task}" added.')
    
    elif choice == '2':
        if not tassks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tassks, start=1):
                print(f"{idx}. {task}")
    
    elif choice == '3':
        if not tassks:
            print("No tasks to remove.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tassks, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tassks):
                    removed_task = tassks.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    
    else:
        print("Invalid choice. Please try again.")
    
    print()  # Print a newline for better readability   