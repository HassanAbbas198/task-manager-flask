from .repository import TaskRepository

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, data):
        self.task_repository.create_task(data)

        return {'message': 'Task created successfully'}

    def get_tasks(self):
        tasks = self.task_repository.get_tasks()
        return {'data': tasks}

    def get_task(self, task_id):
        task = self.task_repository.get_task(task_id)
        return task
