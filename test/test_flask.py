def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<title>Mountain plan</title>" in response.data
