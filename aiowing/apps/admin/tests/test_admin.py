from aiohttp import ClientSession

from aiowing import settings


async def test_unauthenticated_records(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get(test_app.router['admin_records'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == test_app.router['admin_login'].url()
    await resp.release()


async def test_unauthenticated_login(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.post(test_app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD},
                          allow_redirects=False)
    assert resp.headers.get('Location') == \
        test_app.router['admin_records'].url()
    await resp.release()


async def test_unauthenticated_logout(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get(test_app.router['admin_logout'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == test_app.router['admin_login'].url()
    await resp.release()


async def test_authenticated_records(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.post(test_app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD},
                          allow_redirects=False)
    resp = await cli.get(test_app.router['admin_records'].url(),
                         allow_redirects=False)
    assert resp.status == 200
    await resp.release()


async def test_authenticated_login(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.post(test_app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD},
                          allow_redirects=False)
    resp = await cli.get(test_app.router['admin_login'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == \
        test_app.router['admin_records'].url()
    await resp.release()


async def test_authenticated_logout(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.post(test_app.router['admin_login'].url(),
                          data={'email': settings.SUPERUSER_EMAIL,
                                'password': settings.SUPERUSER_PASSWORD},
                          allow_redirects=False)
    resp = await cli.get(test_app.router['admin_logout'].url(),
                         allow_redirects=False)
    assert resp.headers.get('Location') == test_app.router['admin_login'].url()
    await resp.release()
