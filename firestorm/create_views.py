# -*- coding: utf-8 -*-
#!/usr/bin/env python
# pylint: disable=too-many-ancestors
"""Generic view classes for the models in the firestorm
application.
"""
from __future__ import unicode_literals

from django.views.generic.edit import CreateView

from .models import UserManager, Topic, Interest, Presentation, Feedback


class UserManagerCreate(CreateView):
    model = UserManager
    fields = ['email', 'first_name', 'last_name', 'objects']


class TopicCreate(CreateView):
    model = Topic
    fields = ['subject', 'description', 'depth', 'suggested_by',
              'suggested_date', 'user_interest', 'user_skill_level']


class InterestCreate(CreateView):
    model = Interest
    fields = ['user', 'topic', 'level']


class PresentationCreate(CreateView):
    model = Presentation
    fields = ['topic', 'presenter', 'when', 'feedback']


class FeedbackCreate(CreateView):
    model = Feedback
    fields = ['presentation', 'received_by', 'prep_level', 'comments']

