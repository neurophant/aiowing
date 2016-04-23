import asyncio

from peewee_async import Manager, PooledPostgresqlDatabase

from aiowing.settings import env


loop = asyncio.get_event_loop()

pool = PooledPostgresqlDatabase(
    env.DB_NAME,
    max_connections=env.DB_MAX_CONNECTIONS,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    host=env.DB_HOST,
    port=env.DB_PORT)

manager = Manager(pool, loop=loop)
manager.database.allow_sync = False
