from aiowing import settings
from aiowing.apps.web.models import Record


with settings.manager.allow_sync():
    Record.delete().execute()

    records = []
    for index in range(settings.RECORDS_COUNT):
        if index % 2 == 0:
            active = True
        else:
            active = False
        records.append(dict(
            active=active,
            name='record %d' % index,
            description='description %d' % index))

    with settings.atomic():
        Record.insert_many(records).execute()
