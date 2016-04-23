from aiohttp import web
import aiohttp_jinja2
import jinja2

from aiowing.settings import env
from aiowing.settings.routes import routes


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(env.TEMPLATES_PATH))

for route in routes:
    app.router.add_route(*route[0], **route[1])

if env.DEBUG:
    app.router.add_static(env.STATIC_URL, env.STATIC_PATH)

if env.DEBUG:
    web.run_app(app)
