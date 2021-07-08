ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR ./code

RUN python -m pip install Django

RUN python -m pip install psycopg2-binary

EXPOSE 8000