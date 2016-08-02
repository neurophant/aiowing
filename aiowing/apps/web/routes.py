from aiowing.base.route import get
from aiowing.apps.web.handlers import Records


routes = (
    get(r'/', Records, 'records'),
    get(r'/{page:([1-9]\d*)}/', Records, 'records_page'),
    get(r'/{page:([1-9]\d*)}', Records)
)
