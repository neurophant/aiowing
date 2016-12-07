from aiowing.base.route import get
from aiowing.apps.web.handlers import Records


routes = (
    get(r'/', Records, 'web_records'),
    get(r'/{page:([1-9]\d*)}/', Records, 'web_records_page'),
    get(r'/{page:([1-9]\d*)}', Records))
