import argparse

from aiohttp import web

from aiowing.application import create_app


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    web.run_app(create_app(), port=args.port)
