# -*- coding: utf-8 -*-
# pylint: disable=unused-wildcard-import, wildcard-import
from __future__ import unicode_literals

from .settings_base import *

ALLOWED_HOSTS = ['127.0.0.1', 'testserver']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WEBSERVER = 'http://127.0.0.1:8000'
DB1 = 'localhost'
ENVIRONMENT = 'DEVELOPMENT'

try:
    from .dev_local import *
except ImportError:
    pass
