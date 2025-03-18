#!/bin/bash

# Enviroment variables
echo "DB_ENGINE: $DB_ENGINE"
echo "DB_HOST: $DB_HOST"
echo "DB_PORT: $DB_PORT"
echo "DB_NAME: $DB_NAME"
echo "DB_USER: $DB_USER"
echo "DB_PASSWORD: $DB_PASSWORD"
echo "DB_DRIVER: $DB_DRIVER"


# Start cron service
# nohup service cron start > /dev/null 2>&1 &

# Start ssh service
nohup service ssh start > /dev/null 2>&1 &


# Set root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set HOST and PORT
HOST=${HOST:-'0.0.0.0'}
PORT=${PORT:-'8000'}

# Wait for the database
sleep 15


# Database

# Migrate database
echo 'Migrating database...'
conda run --no-capture-output -n gdadc alembic revision --autogenerate

# Upgrade database
echo 'Upgrading database...'
conda run --no-capture-output -n gdadc alembic upgrade head


# API

# Run API
echo 'Running API'
conda run --no-capture-output -n gdadc uvicorn app.main:app --reload --host $HOST --port $PORT
