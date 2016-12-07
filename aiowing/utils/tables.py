from aiowing import settings
from aiowing.apps.web.models import Record
from aiowing.apps.admin.models import User


tables = (Record, User)

with settings.manager.allow_sync():
    settings.pool.drop_tables(tables, safe=True, cascade=True)
    settings.pool.create_tables(tables, safe=True)
