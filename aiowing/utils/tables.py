from aiowing.settings.db import pool, manager
from aiowing.apps.web.models import Record


tables = (Record, )

with manager.allow_sync():
    pool.drop_tables(tables, safe=True, cascade=True)
    pool.create_tables(tables, safe=True)
