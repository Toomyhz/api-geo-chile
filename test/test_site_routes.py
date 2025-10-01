import pytest

def test_render_home(client):
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    assert "División Político Administrativa de Chile" in html

def test_render_docs(client):
    response = client.get("/api/docs/")
    html = response.data.decode("utf-8")
    assert "Docs - API Geo Chile" in html