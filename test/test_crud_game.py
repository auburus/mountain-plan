def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<title>Ya te vale</title>" in response.data
