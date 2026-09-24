from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_invalid_file_path():
    payload = {
        "file_path": "invalid_path.csv",
        "filters": [
            {

              "column":"columns",
              "operator":"==",
              "value":"any"
            }
        ]
    }

    response = client.post("/query", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "file not found"

def test_invalid_operator():
    payload = {
        "file_path": "uploaded_csv/employees.csv",
                "filters": [
                    {
        
                      "column":"department",
                      "operator":"operator",
                      "value":"HR"
                    }
                ]
    }

    response = client.post("/query", json=payload)
    assert response.status_code == 422



def test_valid_query():
    payload = {
        "file_path": "uploaded_csv/sales.csv",
        "filters": [
            {

              "column":"product",
              "operator":"==",
              "value":"electronics"
            }
        ]
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 400

