# -*- coding: utf-8 -*-
"""views.py represents the user-interface Pythonic logic.

This is the views.py which represents the Python logic for views
that refer specifically to a user's interaction with the application.
Kiosk views are held in another file and do not belong in here.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    """index is the main entrypoint of the user experience.

    I suspect this will ultimately have some sort of dashboard that allows
    the end-user to then make changes to the content presented to him/her.
    """
    return render(request, 'user/index.html', {})

@login_required
def voting(request):
    """voting is where people can login to regerster intererst blah blah

    {mckay add stuff here}
    """
    return render(request, 'user/voting.html', {})
