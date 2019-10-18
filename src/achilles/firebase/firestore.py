from google.cloud.exceptions import NotFound
from firebase_admin import firestore
from . import config

import os

class Firestore():

    def __init__(self):
        self.default_app = config.configure_firebase_admin()
        self.db = firestore.client()

    def get_last_media_by(self, account_id, entity):
        try:
            collection_ref = self.db.collection('medias')

            where = [
                ('account_id', '==', str(account_id)),
                ('entity', '==', entity)
            ]

            for param in where:
                collection_ref = collection_ref.where(param[0], param[1], param[2])

            docs = collection_ref.order_by(
                'published_date',
                direction=firestore.Query.ASCENDING
            ).limit(1).stream()

            media = None
            for doc in docs:
                media = doc.to_dict()

            return media
        except NotFound:
            print('No such document at account={} => entity{}'.format(account_id, entity))
