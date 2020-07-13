web: gunicorn server:app
worker: celery worker -A app.celery --loglevel=info
