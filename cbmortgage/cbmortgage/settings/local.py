from .base import *
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = '#u(=-8d(up2@63u&jhn5*kebh@ti8npkuk^2i%fhbp*shkc5xg'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}