from aiowing.base.route import get, post
from aiowing.apps.admin.handlers import Login, Logout, Records


routes = (
    get(r'/admin/login/', Login, 'admin_login'),
    post(r'/admin/login/', Login, 'admin_login_post'),
    get(r'/admin/logout/', Logout, 'admin_logout'),

    get(r'/admin/', Records, 'admin_records'),
    post(r'/admin/', Records, 'admin_records_post'),
)
