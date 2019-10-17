from flask import Flask, jsonify

from .views import (
    app as achilles,
    medias,
)


def create_app():
    app = Flask(__name__)
    medias.configure(app)
    achilles.configure(app)

    return app
