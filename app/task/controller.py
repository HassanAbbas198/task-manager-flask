from flask import Blueprint, jsonify
from .service import TaskService

task_bp = Blueprint('task', __name__)
task_service = TaskService()


@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = task_service.get_tasks()
    return jsonify(tasks)
