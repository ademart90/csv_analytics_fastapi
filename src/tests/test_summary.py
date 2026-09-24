from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_invalid_summary():
    
    payload = {"file_path": "invalid_path.csv"}
    response = client.post("/summary", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "file not found"

def test_valid_summary():

    payload ={"file_path": "uploaded_csv/employees.csv"}
    response = client.post("/summary", json=payload)
    assert response.status_code == 200