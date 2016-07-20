import psycopg2
import peewee
from aiohttp import web
from aiohttp_session import get_session

from aiowing.settings import db
from aiowing.apps.admin.models import User


class Handler(web.View):
    async def get_current_user(self):
        """
        Current user
        """
        session = await get_session(self.request)
        email = session.get('email', None)

        if email is None:
            return None

        try:
            user = await db.manager.get(
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

    async def paging(self, page, page_count):
        if page > page_count:
            page = page_count

        if page < 1:
            page = 1

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        if page < page_count:
            next_page = page + 1
        else:
            next_page = None

        return prev_page, page, next_page

    async def ajax_empty(self, status):
        return web.json_response(dict(status=status))
