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
