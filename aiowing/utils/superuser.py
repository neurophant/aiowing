from aiowing import settings
from aiowing.apps.admin.models import User


with settings.manager.allow_sync():
    user = User.create(
        active=True,
        superuser=True,
        email=settings.SUPERUSER_EMAIL,
        password=settings.SUPERUSER_PASSWORD)

if user:
    print(user.uid, user.uts, user.active, user.superuser, user.email,
          user.check_password(password=settings.SUPERUSER_PASSWORD))
else:
    print(None)
