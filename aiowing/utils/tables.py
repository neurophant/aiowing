from aiowing.settings.db import pool, manager
from aiowing.apps.web.models import Record
from aiowing.apps.admin.models import User


tables = (Record, User, )

with manager.allow_sync():
    pool.drop_tables(tables, safe=True, cascade=True)
    pool.create_tables(tables, safe=True)
