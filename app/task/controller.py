from flask import Blueprint, jsonify, request
from app.error_handlers import error_formatter
from .service import TaskService
from .exceptions import TaskNotFoundError, ValidationError
from .schemas import CreateTaskSchema, UpdateTaskSchema

task_bp = Blueprint('task', __name__)
task_service = TaskService()
create_task_schema = CreateTaskSchema()
update_task_schema = UpdateTaskSchema()


@task_bp.route('/', methods=['POST'])
def create_task():
    try:
        data = request.json

        errors = create_task_schema.validate(data)
        if errors:
            raise ValidationError(message=str(errors))

        response = task_service.create_task(data)
        return jsonify({'data': response}), 201
    except ValidationError as e:
        return error_formatter(400, str(e))


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
    try:
        data = request.json

        errors = update_task_schema.validate(data)
        if errors:
            raise ValidationError(message=str(errors))

        response = task_service.update_task(task_id, data)
        return jsonify({'data': response})
    except ValidationError as e:
        return error_formatter(400, str(e))
    except TaskNotFoundError as e:
        return error_formatter(404, str(e))


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        response = task_service.delete_task(task_id)
        return jsonify({'data': response})
    except TaskNotFoundError as e:
        return error_formatter(404, str(e))
