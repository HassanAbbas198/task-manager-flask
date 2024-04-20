class TaskNotFoundError(Exception):
    def __init__(self, message='Task not found'):
        self.message = message
        super().__init__(self.message)
