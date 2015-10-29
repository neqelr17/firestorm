# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

#http://stackoverflow.com/a/2180209
@register.filter
def currency(dollars):
    if dollars == 0:
        return "-"
    dollars = round(float(dollars), 2)
    return "%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
