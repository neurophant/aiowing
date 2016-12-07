import datetime

import peewee

from aiowing import settings


class Model(peewee.Model):
    """Common db model"""

    uid = peewee.PrimaryKeyField(unique=True, index=True)
    uts = peewee.DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        database = settings.pool
        order_by = ('-uts', )
