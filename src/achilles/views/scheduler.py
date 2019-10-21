from flask import Blueprint, jsonify
from redis import Redis
from rq import Queue


bp = Blueprint('schedulers', __name__)
queue = Queue('kratos-app', connection=Redis.from_url('redis://'))


@bp.route("/schedulers")
def get_schedulers():
    job = queue.enqueue('core.app.get_schedulers')

    while not job.is_finished:
        job.refresh()

    print(job.meta)

    return jsonify({
        'status': 200,
        'job_id': job.get_id(),
        'job': job.meta,
    })


@bp.route("/scheduler/accounts/<uuid:account_id>/entities/<int:entity>/start")
def scheduler_start(account_id, entity):
    interval = 30
    job = queue.enqueue('core.app.add_queue', interval, account_id, entity)

    while not job.is_finished:
        job.refresh()
        print(job.meta)

    return jsonify({
        'account_id': account_id,
        'entity': entity,
        'status': 200,
        'job_id': job.get_id(),
        'job': job.meta,
    })


@bp.route("/scheduler/<uuid:job_id>/stop")
def scheduler_stop(job_id):
    queue = Queue('kratos-app', connection=Redis.from_url('redis://'))

    job = queue.enqueue('core.app.remove_queue', str(job_id))
    while not job.is_finished:
        job.refresh()
        print(job.meta)

    return jsonify({
        'status': 200,
        'job': job.get_id(),
        'job_removed': job.meta
    })


def configure(app):
    app.register_blueprint(bp)
