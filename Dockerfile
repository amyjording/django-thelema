# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* /code/
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . /code/