web: gunicorn final.wsgi

release: python manage.py collectsatic --noinput  & python manage.py migrate 