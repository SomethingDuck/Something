class Task:
    def __init__(self, name, description, state, deadline):
        self.name = name
        self.description = description
        self.state = state
        self.deadline = deadline

    def is_it_completed(self):
        if self.state == "Completed":
            print("Task " + self.name + " is Completed")
        else:
            print("Task " + self.name + " is not Completed")

    def show_description(self):
        print("Task description is: " + self.description)

class TaskManager(Task):
    def __init__(self, name, description, state, deadline):
        super().__init__(name, description, state, deadline)

task1 = TaskManager("Task1", "No description yet", "Uncompleted", 12.8)
task2 = TaskManager("Task2", "No pancakes for you", "Completed", 8.3)

task1.is_it_completed()
task2.show_description()
