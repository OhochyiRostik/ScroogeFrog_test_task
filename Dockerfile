FROM python:3.11-alpine3.19

COPY requirements.txt /temp/requirements.txt

WORKDIR /drf_test_task_app

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password drf_test_task_app-user

COPY drf_test_task_app /drf_test_task_app

USER drf_test_task_app-user
