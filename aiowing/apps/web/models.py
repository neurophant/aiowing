import peewee

from aiowing.base import model


class Record(model.Model):
    """Record db model"""

    active = peewee.BooleanField(default=True)

    name = peewee.CharField(max_length=256, index=True, unique=True)
    description = peewee.TextField(null=True)

    class Meta:
        indexes = ((('active', 'name'), True), )
