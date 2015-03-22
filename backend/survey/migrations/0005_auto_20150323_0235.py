# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_event_approve_email_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_notified',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='approve_email_content',
            field=models.TextField(help_text='\uccab \uc904\uc740 \uc81c\ubaa9', null=True, blank=True),
            preserve_default=True,
        ),
    ]
