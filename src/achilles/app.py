from flask import Flask, jsonify
from flask_uuid import FlaskUUID

from .views import (
    app as achilles,
    medias,
)


def create_app():
    app = Flask(__name__)

    FlaskUUID(app)

    medias.configure(app)
    achilles.configure(app)

    return app
