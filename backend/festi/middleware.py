from django.http import QueryDict

class PutMethodMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'PUT':
            request.PUT = QueryDict(request.body)
        else:
            request.PUT = QueryDict('')

