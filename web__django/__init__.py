# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

# 10/29/15 - DE - Disabled because this project isn't using celery
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
#from .celeryapp import app as celery_app
