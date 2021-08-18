ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR /code

RUN python -m pip install --upgrade pip

COPY requirements.txt /code/requirements.txt

RUN python -m pip install -r requirements.txt
