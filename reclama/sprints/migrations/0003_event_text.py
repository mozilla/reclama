# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0002_auto_20150130_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
