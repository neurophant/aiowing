async def test_records(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get(test_app.router['web_records'].url(),
                         allow_redirects=False)
    assert resp.status == 200
    await resp.release()


async def test_records_not_fount(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get(
        test_app.router['web_records_page'].url(parts={'page': 0}),
        allow_redirects=False)
    assert resp.status == 404
    await resp.release()
