"""
WSGI config for invent project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settingModule = "invent.settings." + os.getenv('SERVER_ENV') if os.getenv(
    'SERVER_ENV') is not None else "invent.settings.local"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settingModule)


application = get_wsgi_application()