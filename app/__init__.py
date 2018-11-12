from flask import Flask

from app.config import configs


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])

    # Register all your endpoints here.
    # from views import ....
    # app.register_blueprint()

    # from resources import ....
    # app.register_blueprint()

    return app
