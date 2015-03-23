from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

try:
    from settings_local import *
except ImportError:
    pass
