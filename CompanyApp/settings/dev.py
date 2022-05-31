from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    str(BASE_DIR) + '/home/'
]

INSTALLED_APPS = INSTALLED_APPS + ['django_extensions', 'sslserver', ]

INTERNAL_IPS = ["localhost", "127.0.0.1"]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

ALLOWED_HOSTS = ["*"]