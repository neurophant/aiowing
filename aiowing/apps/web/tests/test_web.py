async def test_200(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.get(app.router['web_records'].url(),
                         allow_redirects=False)
    assert resp.status == 200


async def test_404(loop, test_app, test_client):
    app = test_app(loop)
    cli = await test_client(app)
    resp = await cli.get(
        app.router['web_records_page'].url(parts={'page': 0}),
        allow_redirects=False)
    assert resp.status == 404
