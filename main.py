import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_all_data(a):
    response = a.get('/data')
    assert response.status_code == 200

