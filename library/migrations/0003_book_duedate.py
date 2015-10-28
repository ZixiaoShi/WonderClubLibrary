# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151028_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='duedate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
