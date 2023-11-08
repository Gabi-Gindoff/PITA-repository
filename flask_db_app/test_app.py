import pytest
from dapp import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Data from SQLite Database" in response.data  # Update the expected text

def test_add_data(client):
    response = client.get('/add_data')
    assert response.status_code == 200
    assert b"Add Help Desk Ticket" in response.data  # Update the expected text

def test_add_data_post(client):
    data = {
        'question': 'How do I use pytest?',
        'response': 'You can use pytest for testing Python applications.',
        'responseDate': '2023-10-31',
        'category': 'Testing'
    }
    response = client.post('/add_data', data=data, follow_redirects=True)
    
    # Check if the status code is a successful status code (e.g., 200 or 302 for redirection)
    assert response.status_code in (200, 302)

def test_non_existent_route(client):
    response = client.get('/non_existent_route')
    assert response.status_code == 404

def test_read_data_from_database(client):
    # Assuming you have some data in your database, retrieve it
    response = client.get('/')
    
    # Check if the status code is a successful status code (e.g., 200 or 302 for redirection)
    assert response.status_code in (200, 302)
    
    # Check if the data you expect from the database is present in the response data
    assert b"Ticket ID: 1" in response.data
