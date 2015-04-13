# coding: utf8
import csv
from codecs import BOM_UTF8
import os
import random
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import force_unicode, smart_str
from jsonfield import JSONField


def random_name(instance, filename):
    cls_name = instance.__class__.__name__.lower()
    dirpath_format = cls_name + '/%Y/%m/%d/%H%M'
    dirpath = os.path.normpath(force_unicode(timezone.now().strftime(smart_str(dirpath_format))))
    random_name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789', 10))
    extension = os.path.splitext(filename)[-1]
    return dirpath + '_' + random_name + extension


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(Base):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, db_index=True)
    props = JSONField(verbose_name='Questions', blank=True)
    begin = models.DateTimeField()
    end = models.DateTimeField()
    is_public = models.BooleanField(default=False, db_index=True)
    approve_email_content = models.TextField(blank=True, null=True, help_text=u'첫 줄은 제목')

    def __unicode__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'props': self.props,
            'begin': self.begin,
            'end': self.end,
        }

    def export_csv(self, f):
        header = ['email', 'name', 'gender', 'is_approved', 'is_notified', 'is_attended']


        f.write(BOM_UTF8)
        writer = csv.writer(f)
        writer.writerow([(col or '').encode('utf8') for col in header])

        for survey in self.survey_set.select_related('user').all():
            try:
                social = survey.user.socialaccount_set.first()
                name = social.extra_data['name']
                gender = social.extra_data['gender']
            except (AttributeError, KeyError):
                name = ''
                gender = ''

            row = [survey.user.email, name, gender, survey.is_approved, survey.is_notified, survey.is_attended]
            row.extend([prop['answer'] for prop in survey.props])
            writer.writerow([(col or '').encode('utf8') for col in row])

        return f


class Speaker(models.Model):
    event = models.ForeignKey(Event)
    idx = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to=random_name)
    keyword = models.CharField(max_length=20, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    detail = models.TextField(blank=True)

    class Meta:
        ordering = ('idx', 'id')


class Survey(Base):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    props = JSONField()
    is_approved = models.BooleanField(default=False, db_index=True, verbose_name=u'승인여부')
    is_notified = models.BooleanField(default=False, db_index=True, verbose_name=u'알림여부')
    is_attended = models.BooleanField(default=False, db_index=True, verbose_name=u'참석여부')

    class Meta:
        unique_together = (('event', 'user'),)

    def as_dict(self):
        return {
            'props': self.props,
            'is_approved': self.is_approved,
            'is_notified': self.is_notified,
            'is_attended': self.is_attended,
        }

