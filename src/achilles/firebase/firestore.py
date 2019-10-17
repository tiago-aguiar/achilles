from firebase_admin import firestore
from . import config

import os

class Firestore():

    def __init__(self):
        self.default_app = config.configure_firebase_admin()
        self.db = firestore.client()


    def create_document(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)


    def get_document(self, collection, document):
        doc_ref = self.db.collection(collection).document(document)
        try:
            return doc_ref.get()
        except google.cloud.exceptions.NotFound:
            print(u'No such document at {} => {}'.format(collection, document))


    def get_document_by(self, collection, wheres):
        collection_ref = self.db.collection(collection)
        for where in wheres:
            collection_ref = collection_ref.where(where[0], where[1], where[2])

        try:
            return collection_ref.stream()
        except google.cloud.exceptions.NotFound:
            print(u'No such document at {} => {}'.format(collection, wheres))


