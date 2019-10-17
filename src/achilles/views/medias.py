from flask import Blueprint, jsonify
from ..firebase.firestore import Firestore

bp = Blueprint('medias', __name__)
firestore = Firestore()

@bp.route("/accounts/<uuid:account_uuid>/entities/<int:entity>/medias/next")
def next_media(account_uuid, entity):
    wheres  = [
        ('account_id', '==', str(account_uuid)),
        ('entity', '==', entity)
    ]

    medias = []
    docs = firestore.get_document_by('medias', wheres)
    for doc in docs:
        medias.append(doc.to_dict())

    return jsonify({'account_uuid': account_uuid, 'medias': medias})


def configure(app):
    app.register_blueprint(bp)

