from .repository import TaskRepository
from .exceptions import TaskNotFoundError


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
        if not task:
            raise TaskNotFoundError(f'Task with id {task_id} not found')

        return task

    def update_task(self, task_id, data):
        task = self.task_repository.get_task(task_id, False)

        task.title = data.get('title')
        task.description = data.get('description')
        task.completed = bool(data.get('completed'))

        self.task_repository.update_task()

        return {'message': 'Task updated successfully'}

    def delete_task(self, task_id):
        task = self.task_repository.get_task(task_id, False)

        self.task_repository.delete_task(task)

        return {'message': 'Task deleted successfully'}
