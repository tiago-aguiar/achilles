import pytest

from achilles.app import create_app

@pytest.fixture
def app():
    return create_app()
