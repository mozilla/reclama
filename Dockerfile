FROM python:2.7
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y mysql-client
RUN pip install -r requirements/dev.txt
