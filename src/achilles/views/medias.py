from flask import Blueprint, jsonify, request
from ..firebase.firestore import Firestore

bp = Blueprint('medias', __name__)
firestore = Firestore()


@bp.route("/accounts/<uuid:account_id>/entities/<int:entity>/medias/next")
def next_media(account_id, entity):
    account_id = str(account_id)
    doc = firestore.get_last_media_by(account_id, entity)

    if doc is None:
        return jsonify({
            'account_id': account_id,
            'entity': entity,
            'media_id': None,
            'media': None
        })

    return jsonify({
        'account_id': account_id,
        'entity': entity,
        'media_id': doc.id,
        'media': doc.to_dict()
    })


@bp.route("/accounts/<uuid:account_id>/entities/<int:entity>/media",
          methods=['POST'])
def create_media(account_id, entity):
    json = request.json

    json['account_id'] = str(account_id)
    json['entity'] = entity

    doc = firestore.create_media(json)

    return jsonify({
        'account_id': account_id,
        'entity': entity,
        'media_id': doc.id,
        'media': doc.to_dict()
    })


@bp.route("/medias/<string:media_id>/published",
          methods=['PUT'])
def update_media(media_id):
    doc = firestore.update_published_media(media_id)

    return jsonify({
        'media_id': media_id,
        'media': doc.to_dict()
    })


def configure(app):
    app.register_blueprint(bp)
