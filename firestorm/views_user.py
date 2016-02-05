# -*- coding: utf-8 -*-
"""views_user.py represents the user-interface Pythonic logic.

This is the views_user.py which represents the Python logic for views
that refer specifically to a user's interaction with the application.
Kiosk views are held in another file and do not belong in here.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import TopicForm
from .models import Topic, UserPreferences
from .mixins import AjaxableResponseMixin


@login_required
def home(request):
    """home is the main entrypoint of the user experience.

    I suspect this will ultimately have some sort of dashboard that allows
    the end-user to then make changes to the content presented to him/her.
    """
    topics_unvoted = Topic.objects.exclude(user_prefs__exact=request.user)
    vote_data = UserPreferences.objects.filter(user__exact=request.user)
    context = {'subject_create_form': TopicForm(),
               'topics_unvoted': topics_unvoted,
               'vote_data': vote_data}
    return render(request, 'user/index.html', context)


class TopicCreate(AjaxableResponseMixin, CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.suggested_by = self.request.user
        return super(TopicCreate, self).form_valid(form)
