import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.restapi11 import app 

@pytest.fixture
def a():
    return app.test_client()

def test_all_data(a):
    response = a.get('/data')
    assert response.status_code == 200

