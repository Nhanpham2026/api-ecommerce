# conftest.py (hoặc test setup file)
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pages.auth import AuthClient

@pytest.fixture(scope="session")
def access_token():
    auth_client = AuthClient()
    return auth_client.get_token()