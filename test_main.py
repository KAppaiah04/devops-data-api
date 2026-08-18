from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_health_check():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"status": "healthy","environment": "production"}

def test_validate_success():
    response = client.post("/validate",json={"record_id": 101, "metric_value": 45.5})
    assert response.status_code == 200
    assert response.json()["status"] == "VALID"

def test_validate_failure():
    response = client.post("/validate",json={'record_id': 102, 'metric_value': -5.0})
    assert response.status_code == 400

