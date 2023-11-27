import datetime
import datetime
import json

print("""
---------------------------------------------------------------------------------------
  _____  _______ _______ _______ _     _ _______  ______
 |_____]    |    |_____| |______ |____/  |______ |_____/
 |          |    |     | ______| |    \_ |______ |    \_
                            
                            
                            Task management tool for coders XD
                            
                                               ~by aditya-ig10
---------------------------------------------------------------------------------------     
""")
class Task:
    def __init__(self, description, deadline=None):
        self.description = description
        self.created_at = datetime.datetime.now()
        self.completed = False
        self.deadline = deadline

    def to_dict(self):
        return {
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "deadline": self.deadline,
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict["description"], task_dict["deadline"])
        task.created_at = datetime.datetime.fromisoformat(task_dict["created_at"])
        task.completed = task_dict["completed"]
        return task

class TimeManagementApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline=None):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Task added: {task.description}")
        if task.deadline:
            print(f"Deadline: {task.deadline}")
        self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            print(f"Task completed: {task.description}")
            self.save_tasks()
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Tasks:")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            deadline_info = f" - Deadline: {task.deadline}" if task.deadline else ""
            print(f"{i + 1}. {task.description} ({status}){deadline_info} - Created at: {task.created_at}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task_dict) for task_dict in tasks_data]
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    app = TimeManagementApp()
    app.load_tasks()

    while True:
        print("\n \n=== pTASKER: A Task management tool for coders ===")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: format(YYYY-MM-DD HH:MM): ")
            app.add_task(description, deadline)
        elif choice == "2":
            index = int(input("Enter task index to mark as completed: "))
            app.mark_task_completed(index - 1)
        elif choice == "3":
            app.view_tasks()
        elif choice == "4":
            print("Thanks for Using! See you again : )")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
