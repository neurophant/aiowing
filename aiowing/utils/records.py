from aiowing.settings import env
from aiowing.settings.db import pool, manager
from aiowing.apps.web.models import Record


with manager.allow_sync():
    Record.delete().execute()

    records = []
    for index in range(env.RECORDS_COUNT):
        if index % 2 == 0:
            active = True
        else:
            active = False
        records.append(dict(
            active=active,
            name='record %d' % index,
            description='description %d' % index))

    with pool.atomic():
        Record.insert_many(records).execute()
