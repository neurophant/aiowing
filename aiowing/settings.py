import os
import asyncio

from peewee_async import Manager, PooledPostgresqlDatabase


DEBUG = True

BASE_PATH = os.path.join(os.path.dirname(__file__), '../')

TEMPLATES_PATH = os.path.join(BASE_PATH, 'templates')

STATIC_PATH = os.path.join(BASE_PATH, 'static')
STATIC_URL = '/static'

DB_NAME = os.getenv('AIOWING_DB_NAME')
DB_MAX_CONNECTIONS = 8
DB_USER = os.getenv('AIOWING_DB_USER')
DB_PASSWORD = os.getenv('AIOWING_DB_PASSWORD')
DB_HOST = 'localhost'
DB_PORT = 5432

COOKIE_SECRET = os.getenv('AIOWING_COOKIE_SECRET')

SUPERUSER_EMAIL = os.getenv('AIOWING_SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = os.getenv('AIOWING_SUPERUSER_PASSWORD')

RECORDS_COUNT = 1000
RECORDS_PER_PAGE = 12


def get_pool():
    return PooledPostgresqlDatabase(
        DB_NAME,
        max_connections=DB_MAX_CONNECTIONS,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT)


def get_manager(pool_, loop_):
    manager_ = Manager(pool_, loop=loop_)
    manager_.database.allow_sync = False

    return manager_


loop = asyncio.get_event_loop()
pool = get_pool()

manager = get_manager(pool, loop)
