from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_user():
    response = client.post("/users?name=Fabrice")
    assert response.status_code == 200
    assert response.json()["user"]["name"] == "Fabrice"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "count" in response.json()