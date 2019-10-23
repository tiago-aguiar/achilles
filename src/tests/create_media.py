from flask import json
from achilles.models.config import Entity, Account


def test_create_media_photo_album_ig(app):
    with app.test_client() as client:
        entity = Entity.IG
        account = Account(
            id='da7c5052-170d-4eda-af0d-639f5c443411', name='tiagoaguiar')
        url = '/accounts/{}/entities/{}/media'.format(account.id, entity.value)

        response = client.post(url, json={
            'caption': """
            Indicador de Paginação View Pager\n
            .\n
            .\n
            .\n
            #android #androiddev #androiddeveloper #androiddevelopment #AndroidStudio #programmer #programming #code #coder #coding #learntocode #ubuntu #development #androidapp #androidstudioproject #androidstudiosources #androidstudiotutorials #mobiledeveloper #softwaredeveloper #mobiledevelopment #application #mobile #androiddevelopers #developer #java #kotlin #androidcommunity #programadorandroid #desenvolvimentoandroid
            """,
            'entity': entity.value,
            'folder_path': 'instagram/010',
            'media_file': ['010-1.jpg', '010-2.jpg'],
            'type': 1,
            'repeat': False
        })

        assert response.status_code == 200

        data = json.loads(response.data)

        assert str(account.id) == data['account_id']
        assert 1 == data['entity']

        media = data['media']
        assert 2 == len(media['media_file'])
