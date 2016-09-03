"""
WSGI config for blog_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

import sys
# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/bushitan1/blog_fx/blog_server'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_server.settings")

application = get_wsgi_application()
