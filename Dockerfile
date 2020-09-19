FROM python:3.7.4-slim-buster
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y supervisor

ADD . /usr/src/app
RUN pip install -r requirements.txt \
    && python manage.py db upgrade
# CMD ["python","server.py"]
# CMD ["celery","worker","-A","app.celery","--loglevel=info"]

ENV C_FORCE_ROOT=1

CMD ["/usr/bin/supervisord"]