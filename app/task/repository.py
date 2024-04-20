from app.database.database import db
from .model import Task

class TaskRepository:
    def create_task(self, data):
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
        return task

    def get_tasks(self):
        tasks = Task.query.all()

        serialized_tasks = [task.serialize() for task in tasks]

        return serialized_tasks

    def get_task(self, task_id, serialize=True):
        task = Task.query.get(task_id)
        return task.serialize() if task and serialize else task

    def update_task(self):
        db.session.commit()
    
    def delete_task(self, task):
        db.session.delete(task)
        db.session.commit()
