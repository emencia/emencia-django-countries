# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from os.path import abspath, join

from django.db import migrations


def load_data(apps, schema_editor):
    """
    The source file is http://sql.sh/ressources/sql-pays/sql-pays.csv
    Plus four more countries added manually to complete the list.
    """
    Model = apps.get_model('countries', 'Country')
    Translation = apps.get_model('countries', 'CountryTranslation')

    path = abspath(join(__file__, '..', '..', 'fixtures', 'fr_data.csv'))

    objects = []
    with open(path) as f:
        for _, _, iso, _, name, _ in csv.reader(f):
            try:
                model = Model.objects.get(iso=iso)
            except Model.DoesNotExist:
                continue

            objects.append(Translation(master=model, language_code='fr',
                                       name=name.upper(), printable_name=name))

    if objects:
        Translation.objects.bulk_create(objects)


def unload_data(apps, schema_editor):
    MyModelTranslation = apps.get_model('countries', 'CountryTranslation')
    MyModelTranslation.objects.filter(language_code='fr').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_auto_20161021_1206'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=unload_data),
    ]
