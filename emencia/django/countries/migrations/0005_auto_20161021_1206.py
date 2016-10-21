# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_auto_20161021_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('-level', 'iso3'), 'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='printable_name',
        ),
    ]
