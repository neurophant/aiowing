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
        if 'page' in self.request.match_info:
            page = int(self.request.match_info.get('page'))
        else:
            page = 1

        try:
            records = await db.manager.execute(
                Record
                .select()
                .where(Record.active == True)
                .order_by(Record.name.asc())
                .offset((page-1)*env.RECORDS_PER_PAGE)
                .limit(env.RECORDS_PER_PAGE+1))
        except (psycopg2.OperationalError, peewee.IntegrityError,
                peewee.ProgrammingError):
            records = []

        count = len(records)

        if count == 0 and page != 1:
            return web.HTTPFound(self.request.app.router['records'].url())

        next_page = page + 1 if count > env.RECORDS_PER_PAGE else None
        prev_page = page - 1 if page != 1 else None

        return dict(request=self.request,
                    records=records[:env.RECORDS_PER_PAGE],
                    prev_page=prev_page,
                    page=page,
                    next_page=next_page)
