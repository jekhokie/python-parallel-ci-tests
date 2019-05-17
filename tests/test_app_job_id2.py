import pytest
from app import *

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_root(client):
    """Test the default route."""

    res = client.get('/?job_id=2')
    assert b'Hello World' in res.data
    assert b'Job ID: 2' in res.data
