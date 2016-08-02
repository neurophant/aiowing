from os import path, getenv


DEBUG = True

BASE_PATH = path.join(path.dirname(__file__), '../../')

TEMPLATES_PATH = path.join(BASE_PATH, 'templates')

STATIC_PATH = path.join(BASE_PATH, 'static')
STATIC_URL = '/static'

DB_NAME = getenv('AIOWING_DB_NAME')
DB_MAX_CONNECTIONS = 8
DB_USER = getenv('AIOWING_DB_USER')
DB_PASSWORD = getenv('AIOWING_DB_PASSWORD')
DB_HOST = 'localhost'
DB_PORT = 5432

COOKIE_SECRET = getenv('AIOWING_COOKIE_SECRET')

SUPERUSER_EMAIL = getenv('AIOWING_SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = getenv('AIOWING_SUPERUSER_PASSWORD')

RECORDS_COUNT = 1000
RECORDS_PER_PAGE = 12
