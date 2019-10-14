from .base import *
DEBUG = False
SECRET_KEY = 'a%g%5l_kh@044$3&zbvtdci^j*f_t60%an5%%@3iapisr*q#ow'
ALLOWED_HOSTS = ['citybestmortgage.ca','.citybestmortgage.com']
DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'cbmbwp',
                'USER': 'citybestmysql',
                'PASSWORD': 'Sidhumysql199@cbmb',
                'HOST': 'localhost',
                'PORT': '',
    }
}
