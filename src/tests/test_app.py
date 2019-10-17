
def test_ping_app(app):
    with app.test_client() as client:
        response = client.get('/ping')
        assert response.status_code == 200
