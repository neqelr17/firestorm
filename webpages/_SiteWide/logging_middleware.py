# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import time

from django.conf import settings
from django.db import connection


class LoggingMiddleware(object):
    def process_request(self, request):
        self.start_time = time.time()
        logging.info("START: %s", request.get_full_path())

    def process_response(self, request, response):
        try:
            remote_addr = request.META.get('REMOTE_ADDR')
            if remote_addr in getattr(settings, 'INTERNAL_IPS', []):
                remote_addr = request.META.get('HTTP_X_FORWARDED_FOR') or remote_addr
            user_email = "-"
            extra_log = ""
            if hasattr(request, 'user'):
                user_email = getattr(request.user, 'email', '-')
            req_time = time.time() - self.start_time
            if settings.DEBUG:
                sql_time = sum(float(q['time']) for q in connection.queries) * 1000
                extra_log += " (%s SQL queries, %s ms)" % (len(connection.queries), sql_time)
            logging.info("END: %s", request.get_full_path())
            logging.info("%s %s %s %s %s (%.02f seconds)%s", remote_addr,
                         user_email, request.method, request.get_full_path(),
                         response.status_code, req_time, extra_log)
        except Exception, e:
            logging.error("LoggingMiddleware Error: %s", e)
        return response
