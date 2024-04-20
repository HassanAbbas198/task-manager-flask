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
