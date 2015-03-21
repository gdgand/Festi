# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('props', jsonfield.fields.JSONField(verbose_name=b'Questions', blank=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('is_public', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
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
                ('is_approved', models.BooleanField(default=False, db_index=True)),
                ('event', models.ForeignKey(to='survey.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_type', models.CharField(default=b'facebook', max_length=10, db_index=True, choices=[(b'facebook', b'facebook')])),
                ('uid', models.CharField(max_length=20, db_index=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('profile_image_url', models.URLField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(to='survey.User'),
            preserve_default=True,
        ),
    ]
