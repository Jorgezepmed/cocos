from .base import * 

SECRET_KEY = '_c67ins@90e+yr2a4l&elgr*zq2d)z62ms!6=999w7kcbdq7fu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['67.205.174.67']





# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcocos',
        'USER': 'jorge',
        'PASSWORD': 'toroe',
        'HOST': 'localhost',
        'PORT': '',
    }
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')