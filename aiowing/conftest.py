import pytest

from peewee_async import Manager

from aiowing import settings
from aiowing.application import create_app


@pytest.fixture
def test_app():
    def create_test_app(loop):
        settings.loop = loop
        settings.manager = Manager(settings.pool, loop=settings.loop)
        settings.manager.database.allow_sync = False

        return create_app(loop=loop)

    return create_test_app
