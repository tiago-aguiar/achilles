from achilles.models.config import Entity, Account

from flask import json

import uuid


def test_get_last_media_for_instagram(app):
    with app.test_client() as client:
        entity = Entity.IG
        account = Account(id='0aed82c7-7436-4573-a4c6-90574d578df2', name='achilles')

        assert entity.value == 1
        assert account.name == 'achilles'

        url = '/accounts/{}/entities/{}/medias/next'.format(account.id, entity.value)
        assert url == '/accounts/{}/entities/1/medias/next'.format(account.id)

        response = client.get(url)
        assert response.status_code == 200

        res = json.loads(response.data)

        assert str(account.id) == res['account_uuid']
        assert 2 == len(res['medias'])
        assert "Ola" == res['medias'][0]["caption"]
        assert "Ola2" == res['medias'][1]["caption"]
