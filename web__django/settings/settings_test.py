# -*- coding: utf-8 -*-
# pylint: disable=unused-wildcard-import, wildcard-import
from __future__ import unicode_literals

from .settings_base import *
from .settings_prod import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENVIRONMENT = 'TEST'

try:
    from test_local import *
except ImportError:
    pass

