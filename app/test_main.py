from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/employees/?company=Google")
    assert response.status_code == 200
    for item in response.json():
        assert item["company"] == 'Google'


def test_read_main():
  response = client.get("/api/employees/?company=Google323")
  assert response.status_code == 200
  assert len(response.json()) == 0


def test_read_main():
  response = client.get("/api/employees/")
  assert response.status_code == 422