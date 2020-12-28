FROM python:3.9-alpine

RUN apk update && \
    apk add --virtual build-deps gcc make python3-dev musl-dev && \
    apk add --no-cache mariadb-dev

COPY api /code/api/api
COPY setup.py /code/api/

WORKDIR /code/api
RUN pip install .

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "python:api.wsgi", "api:app"]