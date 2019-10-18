from flask import Blueprint, jsonify
from ..firebase.firestore import Firestore

bp = Blueprint('medias', __name__)
firestore = Firestore()

@bp.route("/accounts/<uuid:account_id>/entities/<int:entity>/medias/next")
def next_media(account_id,entity):

    media = firestore.get_last_media_by(account_id, entity)
    print(media)

    return jsonify({
        'account_id': account_id,
        'entity': entity,
        'media': media
    })


def configure(app):
    app.register_blueprint(bp)

