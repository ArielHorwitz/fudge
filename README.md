# Fudge

A simple file hosting/sharing server.


## Install
```bash
cd path/to/fudge
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd fudge
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email _@_.com
```

Initialize or reset server:
```bash
# Clear all post-installation data
python manage.py flush --noinput && sleep 1 && rm -rf ./media
# Create superuser
python manage.py createsuperuser --username admin --email admin@example.com
```

Run the server:
```bash
python manage.py runserver
```
