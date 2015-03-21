import json
from hashlib import md5
from django.conf import settings
from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, QueryDict
from .encoder import DjangoJSONEncoder


class PutMethodMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'PUT':
            request.PUT = QueryDict(request.body)
        else:
            request.PUT = QueryDict('')


class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, basestring):
            if response and response[0] in ('"', '[', '{'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (dict, list, tuple, QuerySet, Model)):
            json_string = json.dumps(response, cls=DjangoJSONEncoder, ensure_ascii=False)
            return HttpResponse(json_string, content_type='application/json')
        else:
            return response
