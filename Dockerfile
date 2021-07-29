ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR ./code

RUN python -m pip install --upgrade pip

RUN python -m pip install Django requests chess.com django-seed matplotlib pgn_parser pycountry mysqlclient tqdm

EXPOSE 8000
