# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings
import survey.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('props', jsonfield.fields.JSONField(verbose_name=b'Questions', blank=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('is_public', models.BooleanField(default=False, db_index=True)),
                ('approve_email_content', models.TextField(help_text='\uccab \uc904\uc740 \uc81c\ubaa9', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idx', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to=survey.models.random_name)),
                ('topic', models.CharField(max_length=100, blank=True)),
                ('detail', models.TextField(blank=True)),
                ('event', models.ForeignKey(to='survey.Event')),
            ],
            options={
                'ordering': ('idx', 'id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('props', jsonfield.fields.JSONField()),
                ('is_approved', models.BooleanField(default=False, db_index=True, verbose_name='\uc2b9\uc778\uc5ec\ubd80')),
                ('is_notified', models.BooleanField(default=False, db_index=True, verbose_name='\uc54c\ub9bc\uc5ec\ubd80')),
                ('is_attended', models.BooleanField(default=False, db_index=True, verbose_name='\ucc38\uc11d\uc5ec\ubd80')),
                ('event', models.ForeignKey(to='survey.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together=set([('event', 'user')]),
        ),
    ]
