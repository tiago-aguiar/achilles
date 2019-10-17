import unittest

from firebase_admin import firestore
from achilles.firebase.firestore import Firestore

class FirestoreTest(unittest.TestCase):

    def setUp(self):
        self.firestore = Firestore()


    def test_create_document_firestore(self):
        collection = u'ping'
        document = u'hello'
        data = {
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815
        }

        self.firestore.create_document(collection, document, data)
        doc = self.firestore.get_document(collection, document)

        self.assertEqual(data['first'], doc.to_dict()['first'])
        self.assertEqual(data['last'], doc.to_dict()['last'])
        self.assertEqual(data['born'], doc.to_dict()['born'])


    def test_not_found_document(self):
        collection = u'ping'
        document = u'notfound'
        data = {
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815
        }

        self.assertRaises(Exception, self.firestore.get_document(collection, document))


    def test_get_document_filtered(self):
        collection = 'medias'
        account_id = '0aed82c7-7436-4573-a4c6-90574d578df2'
        where_clause = [
            ('account_id', '==', account_id),
            ('entity', '==', 1)
        ]

        docs = self.firestore.get_document_by(collection, where_clause)

        for doc in docs:
            self.assertEqual(doc.to_dict()['account_id'], account_id)
            self.assertEqual(doc.to_dict()['caption'], 'Ola')

            self.assertEqual(doc.to_dict()['account_id'], account_id)
            self.assertEqual(doc.to_dict()['caption'], 'Ola')
