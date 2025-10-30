import pytest
from app import app


@pytest.fixture
def client():
app.testing = True
with app.test_client() as client:
yield client


def test_index_route(client):
response = client.get('/')
assert response.status_code == 200
assert b'Relat' in response.data # verifica parte do título


def test_api_reports(client):
response = client.get('/api/reports')
assert response.status_code == 200
data = response.get_json()
assert isinstance(data, list)
assert 'title' in data[0]
