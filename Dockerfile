FROM python:3.7-slim

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt

RUN mv docker/* /usr/bin/

RUN chmod +x /usr/bin/*
