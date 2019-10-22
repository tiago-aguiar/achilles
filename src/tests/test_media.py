from flask import json
from achilles.models.config import Entity, Account
from achilles.util import firebase_todate

from datetime import datetime, timezone
import uuid


def test_create_media_photo_album_ig(app):
    with app.test_client() as client:
        entity = Entity.IG
        account = Account(
            id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')
        url = '/accounts/{}/entities/{}/media'.format(account.id, entity.value)

        assert entity.value == 1
        assert account.name == 'achilles'

        assert url == '/accounts/0aed82c7-7436-4573-a4c6-90574d578df2/entities/1/media'

        response = client.post(url, json={
            'caption': """
            Test caption
            .
            .
            .
            #test #caption
            """,
            'entity': entity.value,
            'folder_path': 'instagram/004',
            'media_file': ['foto3.jpg', 'foto2.jpg'],
            'type': 1
        })

        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 1 == data['entity']

        media = data['media']
        assert 2 == len(media['media_file'])


def test_get_last_media_for_ig(app):
    with app.test_client() as client:
        entity = Entity.IG
        account = Account(
            id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')
        url = '/accounts/{}/entities/{}/medias/next'.format(
            account.id, entity.value)

        assert entity.value == 1
        assert account.name == 'achilles'

        assert url == '/accounts/0aed82c7-7436-4573-a4c6-90574d578df2/entities/1/medias/next'

        response = client.get(url)
        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 1 == data['entity']

        media = data['media']
        assert 2 == len(media['media_file'])


def test_get_empty_media_for_fb(app):
    with app.test_client() as client:
        entity = Entity.FB
        account = Account(
            id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')
        url = '/accounts/{}/entities/{}/medias/next'.format(
            account.id, entity.value)

        assert entity.value == 2
        assert account.name == 'achilles'

        assert url == '/accounts/0aed82c7-7436-4573-a4c6-90574d578df2/entities/2/medias/next'

        response = client.get(url)
        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 2 == data['entity']

        media = data['media']
        assert media is None


def test_get_media_not_published_yet(app):
    with app.test_client() as client:
        entity = Entity.YT
        account = Account(
            id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')
        url = '/accounts/{}/entities/{}/medias/next'.format(
            account.id, entity.value)

        assert entity.value == 0
        assert account.name == 'achilles'

        assert url == '/accounts/0aed82c7-7436-4573-a4c6-90574d578df2/entities/0/medias/next'

        response = client.get(url)
        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 0 == data['entity']
