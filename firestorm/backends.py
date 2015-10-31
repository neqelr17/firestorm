# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User


class AutoEmailLoginBackend(object):
    """Authenticate against the custom user model with an email unique field.
    """
    def authenticate(self, email=None):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Create a new user.
            user = User(email=email)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
