from flask import json
from achilles.models.config import Entity, Account
from achilles.util import firebase_todate

from datetime import datetime
import uuid


def test_get_last_media_for_instagram(app):
    with app.test_client() as client:
        entity = Entity.IG
        account = Account(id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')
        url = '/accounts/{}/entities/{}/medias/next'.format(account.id, entity.value)

        assert entity.value == 1
        assert account.name == 'achilles'

        assert url == '/accounts/0aed82c7-7436-4573-a4c6-90574d578df2/entities/1/medias/next'

        response = client.get(url)
        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 1 == data['entity']

        media = data['media']
        assert 'Ola' == media['caption']
        assert datetime(2019, 10, 10, 3, 0, 0) == firebase_todate(media['created_date'])
        assert datetime(2019, 10, 10, 3, 0, 0) == firebase_todate(media['published_date'])
        assert 2 == len(media['media_url'])
        assert '/folder1/photo1.jpg' == media['media_url'][0]
        assert '/folder2/photo2.jpg' == media['media_url'][1]

