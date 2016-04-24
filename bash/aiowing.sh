source .env/bin/activate
source bash/env.sh

gunicorn server:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker -w 12
