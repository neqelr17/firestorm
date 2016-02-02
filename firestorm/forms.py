# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from .models import Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'url', 'description', 'depth']
