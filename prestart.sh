#! /usr/bin/env bash

# Let the DB start
echo "postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=require"
until psql "postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=require" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done


# Run migrations
alembic upgrade head


