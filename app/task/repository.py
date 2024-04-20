from app.database.database import db
from .model import Task

class TaskRepository:
    def create_task(self, data):
        title = data.get('title')
        description = data.get('description')

        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task

    def get_tasks(self):
        tasks = Task.query.all()

        serialized_tasks = [task.serialize() for task in tasks]

        return serialized_tasks

    def get_task(self, task_id):
        task = Task.query.get(task_id)
        return task.serialize() if task else None
