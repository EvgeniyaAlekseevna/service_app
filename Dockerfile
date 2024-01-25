FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

COPY service_app /service_app
WORKDIR /service_app
EXPOSE 8000

USER service-user