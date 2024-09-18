import pytest

from app import create_app

@pytest.fixture
def app():
    """Create test app"""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_config(client):
    """Test the test client creation"""
    assert client

def test_explore(client):
    """Test the /explore route"""
    response = client.get('/explore')
    # should redirect to login
    assert response.status_code == 302
    assert '/login' in response.location

def test_login(client):
    """test auth route"""
    response = client.get('/auth/login')
    assert response.status_code == 200
