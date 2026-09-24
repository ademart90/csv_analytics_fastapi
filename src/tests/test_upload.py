from fastapi.testclient import TestClient
from src.main import app
from io import BytesIO

client = TestClient(app)

def test_invalid_upload():
    file_content = b'This is an invalid file format'
    response = client.post("/upload", files={"file":("test.txt", BytesIO(file_content), "text/plain")})
    assert response.status_code == 400
    assert response.json()["detail"] == "upload csv file format"

def test_valid_upload():
    file_content = "id, name, User"
    response = client.post("/upload", files={"file":("test.csv", BytesIO(file_content.encode("utf-8")), "text/csv")})
    assert response.status_code == 200