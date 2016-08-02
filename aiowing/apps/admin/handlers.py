import functools
import operator

import peewee
from aiohttp_session import get_session
from aiohttp import web
import aiohttp_jinja2

from aiowing.settings import env, db
from aiowing.base.handler import Handler
from aiowing.apps.admin.models import User
from aiowing.apps.web.models import Record


def unauthenticated(func):
    async def decorated(self, *args, **kwargs):
        current_user = await self.get_current_user()

        if current_user:
            return web.HTTPFound(
                self.request.app.router['admin_records'].url())
        else:
            return await func(self, *args, **kwargs)

    return decorated


def authenticated(func):
    async def decorated(self, *args, **kwargs):
        current_user = await self.get_current_user()

        if not current_user:
            return web.HTTPFound(
                self.request.app.router['admin_login'].url())
        else:
            return await func(self, *args, **kwargs)

    return decorated


class Login(Handler):
    @unauthenticated
    @aiohttp_jinja2.template('admin/login.html')
    async def get(self):
        return dict(
            request=self.request,
            current_user=await self.get_current_user())

    @unauthenticated
    async def post(self):
        await self.request.post()
        email = self.request.POST.get('email', None)
        password = self.request.POST.get('password', None)

        if email is None or password is None:
            return web.HTTPFound(self.request.app.router['admin_login'].url())

        with db.manager.allow_sync():
            try:
                user = User.get(User.email == email)
            except User.DoesNotExist:
                user = None

        if user:
            if user.active and user.superuser and \
                    user.check_password(password=password):
                session = await get_session(self.request)
                session['email'] = user.email
                return web.HTTPFound(
                    self.request.app.router['admin_records'].url())
            else:
                return web.HTTPFound(
                    self.request.app.router['admin_login'].url())
        else:
            return web.HTTPFound(self.request.app.router['admin_login'].url())


class Logout(Handler):
    @authenticated
    async def get(self):
        session = await get_session(self.request)
        del session['email']

        return web.HTTPFound(self.request.app.router['admin_login'].url())


class Records(Handler):
    async def get_page_context(self, page):
        try:
            count = await db.manager.count(Record.select())
        except (psycopg2.OperationalError, peewee.IntegrityError,
                peewee.ProgrammingError):
            count = 0

        page_count, prev_page, page, next_page = \
            await self.paging(count, env.RECORDS_PER_PAGE, page)

        try:
            records = await db.manager.execute(
                Record
                .select()
                .order_by(
                    Record.active.desc(),
                    Record.uts.desc())
                .paginate(page, paginate_by=env.RECORDS_PER_PAGE))
        except (psycopg2.OperationalError, peewee.IntegrityError,
                peewee.ProgrammingError):
            records = []

        return dict(request=self.request,
                    current_user=(await self.get_current_user()),
                    records=records,
                    count=count,
                    page_count=page_count,
                    prev_page=prev_page,
                    page=page,
                    next_page=next_page)

    async def ajax_page(self, status, page):
        context = await self.get_page_context(page)
        record_list = aiohttp_jinja2.render_string(
            'admin/partials/_record_list.html', self.request, context)

        return web.json_response(
            dict(status=status, record_list=record_list))

    @authenticated
    @aiohttp_jinja2.template('admin/records.html')
    async def get(self):
        try:
            page = int(self.request.GET.get('page', 1))
        except ValueError:
            page = 1

        context = await self.get_page_context(page)

        return context

    @authenticated
    async def post(self):
        await self.request.post()

        create = self.request.POST.get('create', None)
        update = self.request.POST.get('update', None)
        delete = self.request.POST.get('delete', None)

        uid = self.request.POST.get('uid', None)
        active = self.request.POST.get('active', None)
        active = True if active is not None else False
        name = self.request.POST.get('name', None)
        if name is not None:
            name = name.strip()
            if not len(name) > 0:
                name = None
        description = self.request.POST.get('description', None)

        try:
            page = int(self.request.POST.get('page', 1))
        except ValueError:
            page = 1

        if create is not None and \
                active is not None and \
                name is not None:
            with db.manager.allow_sync():
                try:
                    with db.pool.atomic():
                        created = Record.create(
                            active=active,
                            name=name,
                            description=description)
                except peewee.IntegrityError:
                    created = None

            if created:
                response = await self.ajax_page('create', page)
            else:
                response = await self.ajax_empty('not_created')

            return response
        elif update is not None and \
                uid is not None and \
                active is not None and \
                name is not None:
            with db.manager.allow_sync():
                try:
                    with db.pool.atomic():
                        updated = Record\
                            .update(
                                active=active,
                                name=name,
                                description=description)\
                            .where(Record.uid == uid)\
                            .execute()
                except peewee.IntegrityError:
                    updated = None

            if updated:
                response = await self.ajax_page('update', page)
            else:
                response = await self.ajax_empty('not_updated')

            return response
        elif delete is not None and \
                uid is not None:
            with db.manager.allow_sync():
                try:
                    with db.pool.atomic():
                        deleted = Record\
                            .delete()\
                            .where(Record.uid == uid)\
                            .execute()
                except peewee.IntegrityError:
                    deleted = None

            if deleted:
                response = await self.ajax_page('delete', page)
            else:
                response = await self.ajax_empty('not_deleted')

            return response
        else:
            response = await self.ajax_empty('not_command')
            return response
