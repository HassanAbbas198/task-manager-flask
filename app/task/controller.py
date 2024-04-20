from flask import Blueprint, jsonify, request
from app.error_handlers import error_formatter
from .service import TaskService
from .exceptions import TaskNotFoundError

task_bp = Blueprint('task', __name__)
task_service = TaskService()


@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.json
    response = task_service.create_task(data)

    return jsonify({'data': response}), 201


@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = task_service.get_tasks()
    return jsonify({'data': tasks})


@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = task_service.get_task(task_id)
        return jsonify({'data': task})

    except TaskNotFoundError as e:
        return error_formatter(404, str(e))


@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json

    response = task_service.update_task(task_id, data)
    return jsonify({'data': response})


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    response = task_service.delete_task(task_id)
    return jsonify({'data': response})
