FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /freshfoods

ADD . /freshfoods

COPY requirements.txt /freshfoods/requirements.txt

RUN pip install -r requirements.txt

COPY . /freshfoods

EXPOSE 8000

CMD python manage.py runserver