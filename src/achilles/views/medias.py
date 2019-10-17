from flask import Blueprint, jsonify

bp = Blueprint('medias', __name__)


def configure(app):
    app.register_blueprint(bp)

