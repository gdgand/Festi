import types
import uuid
from django.core.serializers.json import DjangoJSONEncoder as OrigDjangoJSONEncoder
from django.db.models import Model
from django.db.models.query import QuerySet


class DjangoJSONEncoder(OrigDjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return tuple(o)
        elif hasattr(o, 'as_dict'):
            return o.as_dict()
        elif hasattr(o, 'as_list'):
            return o.as_list()
        elif isinstance(o, Model):
            return {
                'id': o.id,
                'message': 'not implemented as_dict()',
            }
        elif isinstance(o, types.GeneratorType):
            return tuple(o)
        elif isinstance(o, QuerySet):
            return tuple(o)
        elif isinstance(o, uuid.UUID):
            return o.hex
        return super(DjangoJSONEncoder, self).default(o)
