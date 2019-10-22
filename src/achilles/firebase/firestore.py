from google.cloud.exceptions import NotFound
from firebase_admin import firestore
from . import config

import os

from datetime import datetime, timezone


class Firestore():

    def __init__(self):
        self.default_app = config.configure_firebase_admin()
        self.db = firestore.client()

    def update_published_media(self, media_id):
        doc_ref = self.db.collection('medias').document(media_id)
        doc_ref.set({
            'published_date': datetime.utcnow()
        }, merge=True)
        doc = doc_ref.get()
        return doc

    def update_media(self, media_id, data):
        doc_ref = self.db.collection('medias').document(media_id)
        doc_ref.set(data, merge=True)
        doc = doc_ref.get()
        return doc

    def create_media(self, data):
        doc_ref = self.db.collection('medias').document()

        published_date = datetime(2002, 1, 1, 0, 0, 0)
        data['created_date'] = datetime.utcnow()
        data['published_date'] = published_date.replace(tzinfo=timezone.utc)

        doc_ref.set(data)
        doc = doc_ref.get()
        return doc

    def get_last_media_by(self, account_id, entity):
        try:
            collection_ref = self.db.collection('medias')

            where = [
                ('account_id', '==', account_id),
                ('entity', '==', entity)
            ]

            for param in where:
                collection_ref = collection_ref.where(
                    param[0], param[1], param[2])

            docs = collection_ref.order_by(
                'published_date',
                direction=firestore.Query.ASCENDING
            ).limit(1).stream()

            document = None
            for doc in docs:
                document = doc

            return document
        except NotFound:
            print('No such document at account={} => entity{}'.format(
                account_id, entity))
