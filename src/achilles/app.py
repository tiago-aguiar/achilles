from flask import Flask, jsonify
from flask_uuid import FlaskUUID



import rq_dashboard


from .views import (
    app as achilles,
    medias,
    scheduler,
)


def create_app():
    app = Flask(__name__)

    FlaskUUID(app)

    medias.configure(app)
    achilles.configure(app)
    scheduler.configure(app)

    app.config.from_object(rq_dashboard.default_settings) # set default settings for rq-dashboard
    app.config.update(REDIS_URL='redis://') # Set URL of Redis server being used by Redis Queue
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rqstatus")

    return app
