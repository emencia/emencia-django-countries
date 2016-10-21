# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=128, verbose_name='Official name (CAPS)')),
                ('printable_name', models.CharField(max_length=128, verbose_name='Country name')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='countries.Country', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'country_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'country Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='countrytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
