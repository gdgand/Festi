import os
import random
from django.db import models
from django.utils import timezone
from django.utils.encoding import force_unicode, smart_str


def random_name(instance, filename):
    cls_name = instance.__class__.__name__.lower()
    dirpath_format = cls_name + '/%Y/%m/%d/%H%M'
    dirpath = os.path.normpath(force_unicode(timezone.now().strftime(smart_str(dirpath_format))))
    random_name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789', 10))
    extension = os.path.splitext(filename)[-1]
    return dirpath + '_' + random_name + extension


class Speaker(models.Model):
    idx = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to=random_name)
    topic = models.CharField(max_length=100, blank=True)
    detail = models.TextField(blank=True)

    class Meta:
        ordering = ('idx', 'id')

