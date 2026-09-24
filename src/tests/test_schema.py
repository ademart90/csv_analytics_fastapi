from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_invalid_schema():
    invalid_file = "invalid_file.csv"
    response = client.get("/schema", params={"file_name":invalid_file})
    assert response.status_code == 404
    assert response.json()["detail"] == "file not found"

def test_valid_schema():
    valid_file = "uploaded_csv/employees.csv"
    response = client.get("/schema", params={"file_name":valid_file})
    assert response.status_code == 200
