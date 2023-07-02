# Fudge

A simple file hosting/sharing server.


## Install

### From Docker Image
```bash
docker run -it -p 8000:8000 \
    -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
    -e DJANGO_SUPERUSER_USERNAME=admin \
    -e DJANGO_SUPERUSER_PASSWORD=admin \
    fudge-latest
```

### From Source
```bash
cd path/to/fudge
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd fudge
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```

Reset all data:
```bash
# Clear all post-installation data and recreate superuser
python manage.py flush --noinput && sleep 1 && rm -rf ./media
python manage.py createsuperuser --username admin --email admin@example.com
```

Run the server:
```bash
python manage.py runserver
```

Build a docker image:
```bash
python manage.py flush --noinput && sleep 1 && rm -rf ./media
docker build -t fudge-latest /path/to/fudge/
```
