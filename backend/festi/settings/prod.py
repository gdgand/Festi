import os
from .common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from settings_local import *
except ImportError:
    pass
