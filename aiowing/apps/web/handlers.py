import aiohttp_jinja2
import peewee
import psycopg2
from aiohttp import web

from aiowing.settings import env, db
from aiowing.base import handler
from aiowing.apps.web.models import Record


class RecordsHandler(handler.Handler):
    @aiohttp_jinja2.template('web/records.html')
    async def get(self):
        page = self.request.match_info.get('page', None)
        try:
            page = int(page)
        except (TypeError, ValueError):
            page = 1

        try:
            count = await db.manager.count(
                Record
                .select()
                .where(Record.active == True))
        except (psycopg2.OperationalError, peewee.IntegrityError,
                peewee.ProgrammingError):
            count = 0

        page_count, prev_page, page, next_page = await self.paging(
            page, count, env.RECORDS_PER_PAGE)

        try:
            records = await db.manager.execute(
                Record
                .select()
                .where(Record.active == True)
                .order_by(Record.name.asc())
                .paginate(
                    page,
                    paginate_by=env.RECORDS_PER_PAGE))
        except (psycopg2.OperationalError, peewee.IntegrityError,
                peewee.ProgrammingError):
            records = []

        return dict(request=self.request,
                    records=records,
                    page_count=page_count,
                    prev_page=prev_page,
                    page=page,
                    next_page=next_page)
