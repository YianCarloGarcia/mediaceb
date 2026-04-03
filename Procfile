web: gunicorn sistema.wsgi --bind 0.0.0.0:8080
release: python manage.py collectstatic --noinput && python manage.py migrate