from os import path


DEBUG = True

BASE_PATH = path.join(path.dirname(__file__), '../../')

TEMPLATES_PATH = path.join(BASE_PATH, 'templates')

STATIC_PATH = path.join(BASE_PATH, 'static')
STATIC_URL = '/static'

DB_NAME = 'windseed'
DB_MAX_CONNECTIONS = 8
DB_USER = 'windseed'
DB_PASSWORD = 'windseed'
DB_HOST = 'localhost'
DB_PORT = 5432

RECORDS_PER_PAGE = 48
