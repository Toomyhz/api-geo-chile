
def test_ping(client):
    for _ in range(5):
        resp = client.get("/api/ping/")
        assert resp.status_code ==200
    resp = client.get("/api/ping/")
    assert resp.status_code == 429
    assert b"Too Many Request" in resp.data

def test_error():
    assert 1 == 2