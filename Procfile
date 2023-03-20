web: gunicorn Newsaggregator.wsgi --log-file -
worker: celery -A Newsaggregator worker -l info