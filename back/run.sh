#!/bin/bash

# Set root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Load $DIR/.env
[ -f $DIR/.env ] && source $DIR/.env

# Set HOST and PORT
HOST=${HOST:-'0.0.0.0'}
PORT=${PORT:-'8000'}


# Database

# Migrate database
echo 'Migrating database...'
alembic revision --autogenerate

# Upgrade database
echo 'Upgrading database...'
alembic upgrade head


# API

# Run API
echo 'Running API'
uvicorn app.main:app --reload --host $HOST --port $PORT
