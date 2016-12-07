async def test_200(test_app, test_client):
    cli = await test_client(test_app)
    resp = await cli.get('/admin/')
    assert resp.status == 200
