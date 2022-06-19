import pytest
import requests
from configuration import SERVICE_URL
from src.base_classes.response import Response


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response
