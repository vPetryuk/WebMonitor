FROM python:3.8.6-buster

RUN apt update && apt-get install cron -y
RUN mkdir -p /usr/src/webmonitor
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/webmonitor

COPY ./WebMonitor /usr/src/webmonitor
COPY ./requirements.txt /usr/src/webmonitor/requirements.txt

RUN pip install -r requirements.txt

# django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

EXPOSE 8000

CMD service cron start && python manage.py runserver 0.0.0.0:8000