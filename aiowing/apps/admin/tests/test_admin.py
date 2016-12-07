from aiohttp import ClientSession

from aiowing import settings


async def test_unauthenticated_records(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.get(app.router['admin_records'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == app.router['admin_login'].url()


async def test_unauthenticated_login(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.post(app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD},
                          allow_redirects=False)
    assert resp.headers.get('Location') == app.router['admin_records'].url()


async def test_unauthenticated_logout(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.get(app.router['admin_logout'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == app.router['admin_login'].url()


async def test_authenticated_records(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.post(app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD})
    assert resp.status == 200
