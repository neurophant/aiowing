async def test_200(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get('/')
    assert resp.status == 200


async def test_404(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get('/0/')
    assert resp.status == 404
