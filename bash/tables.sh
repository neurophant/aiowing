source .env/bin/activate
source bash/env.sh

sudo -u postgres psql -c "DROP DATABASE IF EXISTS ${AIOWING_DB_NAME};"
sudo -u postgres psql -c "DROP USER IF EXISTS ${AIOWING_DB_USER};"
sudo -u postgres psql -c "CREATE USER ${AIOWING_DB_USER} WITH PASSWORD '${AIOWING_DB_PASSWORD}';"
sudo -u postgres psql -c "CREATE DATABASE ${AIOWING_DB_NAME} WITH OWNER=${AIOWING_DB_USER} ENCODING='utf-8';"

python -m aiowing.utils.tables
