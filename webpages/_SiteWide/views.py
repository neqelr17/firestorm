# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# shamelessly stolen from: https://github.com/Dimitri-Gnidash/django-js-utils
import json
import sys
import re
import types
from collections import OrderedDict
from StringIO import StringIO

from django.conf import settings
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver
from django.http import HttpResponse

#NOTE: 7/12/2014 I am aware that this thing does not meet all of my pattern finders, but for now I'm cool with it.
RE_KWARG = re.compile(r"(\(\?P\<(.*?)\>.*?\)\)?)") #Pattern for recongnizing named parameters in urls
RE_ARG = re.compile(r"(\(.*?\))") #Pattern for recognizing unnamed url parameters


def load_dutils_js(request):
    js_patterns = OrderedDict()
    handle_url_module(js_patterns, settings.ROOT_URLCONF)
    fHandle = StringIO()
    fHandle.write("dutils.conf.urls = ")
    json.dump(js_patterns, fHandle)
    fHandle.write(';')
    contents = fHandle.getvalue()
    fHandle.close()
    return HttpResponse(content = contents, content_type="text/javascript")


def handle_url_module(js_patterns, module_name, prefix=""):
    """
    Load the module and output all of the patterns
    Recurse on the included modules
    """
    if isinstance(module_name, basestring):
        __import__(module_name)
        root_urls = sys.modules[module_name]
        patterns = root_urls.urlpatterns
    elif isinstance(module_name, types.ModuleType):
        patterns = getattr(module_name, 'urlpatterns')
    else:
        root_urls = module_name
        patterns = root_urls

    for pattern in patterns:
        if issubclass(pattern.__class__, RegexURLPattern):
            if pattern.name:
                full_url = prefix + pattern.regex.pattern
                for chr in ["^", "$"]:
                    full_url = full_url.replace(chr, "")
                #handle kwargs, args
                kwarg_matches = RE_KWARG.findall(full_url)
                if kwarg_matches:
                    for el in kwarg_matches:
                        #prepare the output for JS resolver
                        full_url = full_url.replace(el[0], "<%s>" % el[1])
                #after processing all kwargs try args
                args_matches = RE_ARG.findall(full_url)
                if args_matches:
                    for el in args_matches:
                        full_url = full_url.replace(el, "<>")#replace by a empty parameter name
                js_patterns[pattern.name] = "/" + full_url
        elif issubclass(pattern.__class__, RegexURLResolver):
            if pattern.urlconf_name:
                handle_url_module(js_patterns, pattern.urlconf_name, prefix=prefix + pattern.regex.pattern)
