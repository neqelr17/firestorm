# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import site
"""
WSGI config for django_site project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""
# IMPORTANT NOTE: THE LNDS1 INFRASTRUCTURE IS NOT CURRENTLY USING THIS FILE
# AT ALL, IN ORDER TO COMBINE WITH THE PHP APPLICATION. THE OTHER WSGI
# FILE LIVES IN THE HTDOCS FOLDER.

root_dir = os.path.dirname(os.path.dirname(__file__))
site.addsitedir(root_dir)
os.chdir(root_dir)
from web__django.settings.settings_base import SETTINGS
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS)

import django
django.setup()

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
