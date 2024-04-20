from .repository import TaskRepository

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, data):
        return self.task_repository.create_task(data)

    def get_tasks(self):
        tasks = self.task_repository.get_tasks()
        return {'data': tasks}
