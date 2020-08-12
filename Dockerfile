FROM python:3.8.3-alpine

RUN mkdir /app

RUN apk update\
	&& apk add --no-cache bash\
	&& apk add nginx postgresql postgresql-contrib python3-dev musl-dev\
	&& apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev\
	&& pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py migrate

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000\	
