# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.core.management import call_command

FIXTURE_NAME = 'initial_data.xml'
APP_LABEL = 'countries'
COUNTRY_MODELNAME = 'Country'


def load_fixture(apps, schema_editor):
    """
    Simply load app fixtures using the legacy Django command action
    """
    call_command('loaddata', FIXTURE_NAME, app_label=APP_LABEL) 


def unload_fixture(apps, schema_editor):
    """
    Brutally deleting all 'Country' model entries for reversing operation
    """
    appmodel = apps.get_model(APP_LABEL, COUNTRY_MODELNAME)
    appmodel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
