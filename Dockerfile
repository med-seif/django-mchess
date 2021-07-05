ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR /code

RUN python -m pip install Django

EXPOSE 8000