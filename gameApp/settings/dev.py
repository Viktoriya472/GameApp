from .base import *
import os


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
