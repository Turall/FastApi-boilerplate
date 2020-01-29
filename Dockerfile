FROM  tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app
WORKDIR /app

ENV settings=prod
ENV WORKERS_PER_CORE=2



RUN apt-get update -y &&  pip install --upgrade pip &&  \
    pip install -r requirements.txt && \
    apt-get install -y postgresql-client

