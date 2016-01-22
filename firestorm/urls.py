# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import home, kiosk


urlpatterns = [
    # These are custom to the Firestorm project
    url(r'^$', home,
        name='home'),
    url(r'^kiosk/$', kiosk,
        name='kiosk'),
]
