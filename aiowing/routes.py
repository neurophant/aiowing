from aiowing.apps.web.routes import routes as web_routes
from aiowing.apps.admin.routes import routes as admin_routes


routes = web_routes + admin_routes
