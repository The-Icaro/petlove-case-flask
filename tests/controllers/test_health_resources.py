def test_health_check(client):
    response = client.get('/api/ecommerce/v1/health')

    assert response.status_code == 200
    assert response.json == {"status": "up"}