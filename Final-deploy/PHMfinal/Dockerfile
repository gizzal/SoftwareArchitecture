 FROM python:3
 ENV PYTHONUNBUFFERED 1
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 RUN python manage.py collectstatic --noinput --settings=optimus.settings_staging