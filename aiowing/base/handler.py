import psycopg2
import peewee
from aiohttp import web
from aiohttp_session import get_session

from aiowing import settings
from aiowing.apps.admin.models import User


class Handler(web.View):
    async def get_current_user(self):
        """Current user"""

        session = await get_session(self.request)
        email = session.get('email', None)

        if email is None:
            return None

        try:
            user = await settings.manager.get(
                User
                .select()
                .where(User.email == email))
        except (User.DoesNotExist, psycopg2.OperationalError,
                peewee.IntegrityError, peewee.ProgrammingError):
            user = None

        if user is None:
            return None

        if not user.active or not user.superuser:
            return None

        return email

    async def paging(self, count, per_page, page):
        page_count = int(count / per_page) + int(bool(count % per_page))

        if page > page_count or page < 1:
            return None, None, None

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < page_count else None

        return page_count, prev_page, page, next_page

    async def ajax_empty(self, status):
        return web.json_response(dict(status=status))
