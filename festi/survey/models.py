# coding: utf8
from django.db import models
from jsonfield import JSONField


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(Base):
    AUTH_TYPES = (('facebook', 'facebook'),)
    auth_type = models.CharField(max_length=10, choices=AUTH_TYPES, default='facebook', db_index=True)
    uid = models.CharField(max_length=20, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    profile_image_url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        unique_together = (('auth_type', 'uid'),)

    def __unicode__(self):
        return self.email


class Event(Base):
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


class Survey(Base):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
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

