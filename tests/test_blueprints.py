def test_mongo(client):
    response = client.get('/mongo')
    assert response.data == b'mongo'


def test_orchestrator(client):
    response = client.get('/orchestrator')
    assert response.data == b'orchestrator'