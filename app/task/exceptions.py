class TaskNotFoundError(Exception):
    def __init__(self, task_id):
        self.message = f'Task with id {task_id} not found'
        super().__init__(self.message)


class ValidationError(Exception):
    def __init__(self, message='Missing required fields'):
        Exception.__init__(self)
        self.message = message
        super().__init__(self.message)
