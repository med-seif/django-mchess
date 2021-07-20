ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR ./code

RUN python -m pip install Django requests psycopg2-binary chess.com django-seed matplotlib pgn_parser pycountry

EXPOSE 8000
