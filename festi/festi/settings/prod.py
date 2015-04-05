import os
from .common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from settings_local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['RDS_NAME'],
        'USER': os.environ['RDS_USER'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOST'],
        'PORT': '3306',
    }
}