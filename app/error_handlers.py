from flask import jsonify


def error_formatter(status_code=400, message='Something went wrong'):
    payload = {
        'success': False,
        'status_code': status_code,
        'message': message
    }
    response = jsonify(payload)
    response.status_code = status_code
    return response


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return error_formatter(404, 'Resource not found')

    @app.errorhandler(500)
    def internal_error(error):
        return error_formatter(500, 'Internal server error')
