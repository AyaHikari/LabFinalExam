import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Flask App!"}

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json == {"status": "running", "version": "1.0"}
