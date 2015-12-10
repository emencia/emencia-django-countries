# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso', models.CharField(max_length=2, serialize=False, verbose_name='ISO alpha-2', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Official name (CAPS)')),
                ('printable_name', models.CharField(max_length=128, verbose_name='Country name')),
                ('iso3', models.CharField(max_length=3, null=True, verbose_name='ISO alpha-3')),
                ('numcode', models.PositiveSmallIntegerField(null=True, verbose_name='ISO numeric')),
                ('level', models.PositiveSmallIntegerField(default=0, verbose_name='level')),
            ],
            options={
                'ordering': ('-level', 'printable_name'),
                'db_table': 'country',
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
    ]
