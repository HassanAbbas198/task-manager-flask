from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))


class CreateTaskSchema(TaskSchema):
    pass


class UpdateTaskSchema(TaskSchema):
    completed = fields.Boolean(required=True)
