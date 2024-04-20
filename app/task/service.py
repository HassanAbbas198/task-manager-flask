from .repository import TaskRepository

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, data):
        return self.task_repository.create_task(data)

    def get_tasks(self):
        return {'data': [{'id': 1, 'title': 'Task 1'}, {'id': 2, 'title': 'Task 2'}]}
