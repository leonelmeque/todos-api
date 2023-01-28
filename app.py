from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'protected_app'

    from routes.todo import todos_routes
    from routes.timeline import timeline_routes

    app.register_blueprint(todos_routes, url_prefix="/")
    app.register_blueprint(timeline_routes, url_prefix="/")

    return app
