from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_session import session_middleware

from aiowing import settings, routes
from aiowing.base.middleware import error_middleware


app = web.Application(middlewares=[
    session_middleware(EncryptedCookieStorage(settings.COOKIE_SECRET)),
    error_middleware])
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader(settings.TEMPLATES_PATH))

for route in routes.routes:
    app.router.add_route(*route[0], **route[1])

if settings.DEBUG:
    app.router.add_static(settings.STATIC_URL, settings.STATIC_PATH)

if settings.DEBUG:
    web.run_app(app)
