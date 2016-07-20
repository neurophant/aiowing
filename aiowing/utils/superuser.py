from aiowing.settings.db import manager
from aiowing.settings import env
from aiowing.apps.admin.models import User


with manager.allow_sync():
    user = User.create(
        active=True,
        superuser=True,
        email=env.SUPERUSER_EMAIL,
        password=env.SUPERUSER_PASSWORD)

if user:
    print(user.uid, user.uts, user.active, user.superuser, user.email,
          user.check_password(password=env.SUPERUSER_PASSWORD))
else:
    print(None)
