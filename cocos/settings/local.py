from .base import * 



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','67.205.174.67']





# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcocos',
        'USER': 'jorge',
        'PASSWORD': 'toroe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#Git