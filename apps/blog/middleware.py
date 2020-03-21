#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: middleware.py
@time: 2017/1/19 上午12:36
"""
import time
import logging

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from .documents import ELASTICSEARCH_ENABLED, ElaspedTimeDocumentManager

logger = logging.getLogger(__name__)

class OnlineMiddleware(MiddlewareMixin):

    '''
    https://docs.djangoproject.com/en/2.1/topics/http/middleware/
    '''

    def __call__(self, request):
        ''' page render time '''
        start_time = time.time()
        response = self.get_response(request)
        http_user_agent = request.META.get('HTTP_USER_AGENT', '')

        if 'spider'.upper() not in http_user_agent.upper():
            try:
                cast_time = time.time() - start_time
                if ELASTICSEARCH_ENABLED:
                    time_taken = round((cast_time) * 1000, 2)
                    ElaspedTimeDocumentManager.create(url=request.path, time_taken=time_taken, log_datetime=timezone.now(),
                                                      type='blog', useragent=http_user_agent)
                response.content = response.content.replace(b'<!!LOAD_TIMES!!>', str.encode(str(cast_time)[:5]))
            except Exception as e:
                logger.error(e)
        return response
