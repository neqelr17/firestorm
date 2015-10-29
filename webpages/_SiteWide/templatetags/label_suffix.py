# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()

@register.filter
def custom_label_tag(value, arg):
    return value.label_tag(label_suffix=arg)
