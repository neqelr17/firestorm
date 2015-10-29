# -*- coding: utf-8 -*-
# pylint: disable=unused-wildcard-import, wildcard-import
from __future__ import unicode_literals

from .settings_base import *

ALLOWED_HOSTS = ['testserver']

WEBSERVER = 'http://<insert_name_here>'
DB1 = '<insert_name_here>'
ENVIRONMENT = 'PRODUCTION'
FORCE_ALL_EMAILS_TO_ADMIN = False

try:
    from .prod_local import *
except ImportError:
    pass
