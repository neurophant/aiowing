from aiowing.apps.web.handlers import RecordsHandler


routes = (
    (('GET', r'/', RecordsHandler, ), {'name': 'records'}, ),

    (('GET', r'/page/{page:([1-9]\d*)}/', RecordsHandler, ),
        {'name': 'records_page'}, ),
    (('GET', r'/page/{page:(\d+)}', RecordsHandler, ),
        {}, ), )
