from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    @app.route('/')
    def hello_world():
        return '<p>Hello, World!</p>'

    return app
