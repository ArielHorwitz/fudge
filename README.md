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
# From project root
cd $PROJ_ROOT
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd fudge
# python manage.py makemigrations
# python manage.py migrate
echo "Create admin password:"
python manage.py createsuperuser --username admin --email admin@example.com
```

Run the server:
```bash
cd $PROJ_ROOT/fudge
source ../venv/bin/activate
python manage.py runserver
```

Reset all data:
```bash
cd $PROJ_ROOT/fudge
export DJANGO_SUPERUSER_EMAIL="admin@example.com"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="admin"
source ../venv/bin/activate
python manage.py flush --noinput
rm -rf ./media
python manage.py createsuperuser --no-input
```

Build a docker image:
```bash
# Reset data first!
cd $PROJ_ROOT/fudge
export DJANGO_SUPERUSER_EMAIL="admin@example.com"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="admin"
source ../venv/bin/activate
python manage.py flush --noinput
rm -rf ./media
docker build -t fudge-latest $PROJ_ROOT
```

