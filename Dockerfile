FROM python:2.7-slim

EXPOSE 8000
WORKDIR /code

RUN apt-get update && \
    apt-get install -y build-essential mysql-client libmysqlclient-dev python-dev --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/ /code/requirements/
RUN pip install -r requirements/dev.txt

COPY . /code
