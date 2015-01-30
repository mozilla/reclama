# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='event',
            field=models.ManyToManyField(related_name='bugs', to='sprints.Event'),
            preserve_default=True,
        ),
    ]
