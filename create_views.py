#!/usr/bin/env python
"""Generic view classes for the models in the firestorm
application.
"""

from django.views.generic.edit import CreateView
from myapp.models import UserManager
from myapp.models import Topic
from myapp.models import Interest
from myapp.models import Presentation
from myapp.models import Feedback


class UserManagerCreate(CreateView):
    model = UserManager
    fields = ['email', 'first_name', 'last_name', 'objects']


class TopicCreate(CreateView):
    model = Topic
    fields = ['subject', 'description', 'depth', 'suggested_by', 'suggested_date',
              'user_interest', 'user_skill_level']


class InterestCreate(CreateView):
    model = Interest
    fields = ['user', 'topic', 'level']


class PresentationCreate(CreateView):
    model = Presentation
    fields = ['topic', 'presenter', 'when', 'feedback']


class FeedbackCreate(CreateView):
    model = Feedback
    fields = ['presentation', 'received_by', 'prep_level', 'comments']

# Hope these can all go in the same file!
