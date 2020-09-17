"""
WSGI config for cocos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
SECRET_KEY = '_c67ins@90e+yr2a4l&elgr*zq2d)z62ms!6=999w7kcbdq7fu'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocos.settings')

application = get_wsgi_application()
