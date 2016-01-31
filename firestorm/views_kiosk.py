# -*- coding: utf-8 -*-
"""views_kiosk.py represents the user-interface Pythonic logic.

This is the views_kiosk.py which represents the Python logic for views
that refer specifically to the kiosk-type display which is displayed on the
projector.
User views are held in another file and do not belong in here.
"""
from __future__ import unicode_literals

from django.shortcuts import render


def kiosk(request):
    """kiosk is the display that will be projected on the screen, refreshing
    with updates as others make changes.
    """
    return render(request, 'kiosk/framework.html', {})
