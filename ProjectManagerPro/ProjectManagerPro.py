import datetime

class Project:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        tasks_str = "\n".join([str(task) for task in self.tasks])
        return f"Project: {self.name}\nDescription: {self.description}\nDeadline: {self.deadline}\nTasks:\n{tasks_str}"

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Task: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}"

class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_project(self, project_name):
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def __str__(self):
        return "\n".join([str(project) for project in self.projects])

def main():
    project_manager = ProjectManager()

    # Creating a project
    project1 = Project("Website Development", "Develop a company website", datetime.date(2023, 12, 31))
    task1 = Task("Design Homepage", "Create a design for the homepage", datetime.date(2023, 11, 1))
    task2 = Task("Develop Backend", "Develop the backend of the website", datetime.date(2023, 11, 15))
    project1.add_task(task1)
    project1.add_task(task2)

    project_manager.add_project(project1)

    # Output project details
    print(project_manager)

if __name__ == "__main__":
    main()
