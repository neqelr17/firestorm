# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def home(request):
    return HttpResponse('Hello %s' % request.user.email)
