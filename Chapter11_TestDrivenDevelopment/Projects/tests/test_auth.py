
def test_login(client):
    response = client.post('/login', data={'name': 'admin', 'password': 'Password123!'})

    assert response.status_code == 200