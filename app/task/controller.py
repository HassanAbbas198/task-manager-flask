from flask import Blueprint, jsonify, request
from .service import TaskService

task_bp = Blueprint('task', __name__)
task_service = TaskService()

@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.json
    task_service.create_task(data)
    
    return jsonify({'message': 'Task created successfully'}), 201

@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = task_service.get_tasks()
    return jsonify(tasks)
