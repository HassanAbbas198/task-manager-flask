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

        serialized_tasks = [{'id': task.id, 'title': task.title,
                'description': task.description, 'completed': task.completed} for task in tasks]
   
        return serialized_tasks
