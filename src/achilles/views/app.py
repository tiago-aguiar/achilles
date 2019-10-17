from flask import Blueprint, jsonify

bp = Blueprint('app', __name__)


@bp.route("/ping")
def index():
    return jsonify({'hello': 'app'})


def configure(app):
    app.register_blueprint(bp)
