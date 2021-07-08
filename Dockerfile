ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR ./code

RUN python -m pip install Django requests psycopg2-binary

EXPOSE 8000