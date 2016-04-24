# aiowing

Extendable skeleton for developing async web applications using [aiohttp](https://github.com/KeepSafe/aiohttp), [peewee](https://github.com/coleifer/peewee) wrapped with [peewee-async](https://github.com/05bit/peewee-async) and [aiohttp_jinja2](https://github.com/aio-libs/aiohttp_jinja2)

This is a successor of [windseed](https://github.com/embali/windseed)


## Prerequisites

- Ubuntu 14.10
- PostgreSQL 9.3
- Python 3.5+


## Structure

- **aiowing** - aiowing package
  - **apps** - project's applications folder, each app within its folder has
    - **handlers.py** - app handlers
    - **models.py** - app models
    - **routes.py** - app URLs and routes
  - **base** - base classes
    - **handler.py** - base handler class
    - **model.py** - base model class
  - **settings** - project settings
    - **db.py** - postgresql database pool
    - **env.py** - environment variables from env.sh and paths
    - **routes.py** - project routes
  - **utils** - utility scripts
    - **tables.py** - re-create aiowing tables
    - **records.py** - re-create test records

- **server.py** - aiowing application

- **bash** - utility bash scripts
  - **tables.sh** - re-create aiowing database and tables
  - **records.sh** - re-create test records
  - **aiowing.sh** - run application with Gunicorn

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
bash bash/tables.sh - create tables

bash bash/records.sh - create test records

python server.py - run project (DEBUG=True)

bash scripts/aiowing.sh - run project with Gunicorn (DEBUG=False)

Open http://localhost:8080/
```
