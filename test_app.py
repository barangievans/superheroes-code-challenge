import pytest
from app import app

app.testing = True

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_heroes(client):
    response = client.get('/heroes')
    assert response.status_code == 200  # Check if the response is OK
    assert isinstance(response.json, list)  # Ensure the response is a list

def test_get_hero(client):
    response = client.get('/heroes/1')  # Adjust the ID based on your data
    assert response.status_code == 200  # Check if the response is OK
    assert "name" in response.json  # Ensure the response contains the expected keys

# Add more tests for other endpoints...

if __name__ == "__main__":
    pytest.main()
