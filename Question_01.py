# Question [1]
'''To-Do List Application: Create a command-line or GUI-based to-do list application
that allows users to add, view, and delete tasks. You can also add features like due
dates and priority levels.'''

class Task:
    def __init__(self, description, due_date=None, priority=None):
        # Initialize a task with a description, optional due date, and optional priority
        self.description = description
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        # Initialize a to-do list with an empty list of tasks
        self.tasks = []

    def add_task(self, task):
        # Add a task to the to-do list
        self.tasks.append(task)

    def view_tasks(self):
        # View all tasks in the to-do list
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.description}")
                if task.due_date:
                    print(f"   Due: {task.due_date}")
                if task.priority:
                    print(f"   Priority: {task.priority}")
        else:
            print("No tasks found.")

    def delete_task(self, index):
        # Delete a task from the to-do list by its index
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    # Create a to-do list object
    todo_list = ToDoList()

    while True:
        # Display the main menu
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task to the to-do list
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            # View all tasks in the to-do list
            print("\nAll Tasks:")
            todo_list.view_tasks()
        elif choice == "3":
            # Delete a task from the to-do list
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_task(index)
        elif choice == "4":
            # Exit the program
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Example :
    
# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 1
# Enter task description: Finish project
# Enter due date (optional): 2024-03-20
# Enter priority (optional): High
# Task added successfully.

# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 1
# Enter task description: Call mom
# Enter due date (optional): 
# Enter priority (optional): Medium
# Task added successfully.

# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 2

# All Tasks:
# 1. Finish project
#    Due: 2024-03-20
#    Priority: High
# 2. Call mom
#    Priority: Medium

# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 3
# Enter index of task to delete: 1
# Task deleted successfully.

# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 2

# All Tasks:
# 1. Call mom
#    Priority: Medium

# To-Do List Menu:
# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter your choice: 4
# Exiting program...
