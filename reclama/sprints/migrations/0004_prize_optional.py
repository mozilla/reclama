# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0003_event_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='prize',
            field=models.ForeignKey(related_name='prizes', blank=True, to='sprints.Prize', null=True),
            preserve_default=True,
        ),
    ]
