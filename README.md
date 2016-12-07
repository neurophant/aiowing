# aiowing

Extendable skeleton for developing async web applications using [aiohttp](https://github.com/KeepSafe/aiohttp), [peewee](https://github.com/coleifer/peewee) wrapped with [peewee-async](https://github.com/05bit/peewee-async) and [aiohttp_jinja2](https://github.com/aio-libs/aiohttp_jinja2)

This is a successor of [windseed](https://github.com/embali/windseed)


## Structure

- **aiowing** - aiowing package
  - **base** - base classes
    - **handler.py** - base handler class
    - **middleware.py** - middlewares
    - **model.py** - base model class
    - **route.py** - route get and post helpers
  - **apps** - project applications folder, each app within its folder has
    - **handlers.py** - app handlers
    - **models.py** - app models
    - **routes.py** - app URLs and routes
    - **tests** - tests folder
  - **utils** - utility scripts
    - **tables.py** - re-create aiowing tables
    - **records.py** - re-create test records
    - **superuser.py** - create superuser
  - **settings.py** - project settings
  - **routes.py** - project routes
  - **application.py** - application definition
  - **conftest.py** - common fixtures

- **env.sh** - environment variables (source env.sh)

- **server.py** - aiowing application

- **static** - project static files, mainly Bootstrap 3, robots.txt

- **templates** - project templates


## Install Python 3.5+
```
sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get update

sudo apt-get install python3.5 python3.5-venv python3.5-dev
```

## Setup environment and packages

```
pyvenv-3.5 .env

source .env/bin/activate

pip install -r requirements.txt
```


## Run

```
python -m aiowing.utils.tables - create tables

python -m aiowing.utils.superuser - create superuser

python -m aiowing.utils.records - create test records

python server.py 8080 - run project

Open http://localhost:8080/
```


## Run tests
```
py.test
```
