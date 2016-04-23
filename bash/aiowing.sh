source .env/bin/activate

gunicorn server:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker -w 12
