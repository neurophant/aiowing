import pytest

from aiowing import settings
from aiowing.application import create_app


@pytest.fixture
def test_app(loop):
    settings.loop = loop
    settings.pool = settings.get_pool()
    settings.manager = settings.get_manager(settings.pool, settings.loop)

    return create_app(loop=loop)
