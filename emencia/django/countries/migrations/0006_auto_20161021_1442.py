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
    Country = apps.get_model('countries', 'Country')
    Translation = apps.get_model('countries', 'CountryTranslation')

    path = abspath(join(__file__, '..', '..', 'fixtures', 'data.csv'))
    with open(path) as f:
        for _, numcode, iso, iso3, fr, en in csv.reader(f):
            defaults = {'iso3': iso3, 'numcode': numcode}
            model, created = Country.objects.get_or_create(iso=iso,
                                                           defaults=defaults)

            defaults = {'name': en.upper(), 'printable_name': en}
            Translation.objects.get_or_create(master=model, language_code='en',
                                              defaults=defaults)

            defaults = {'name': fr.upper(), 'printable_name': fr}
            Translation.objects.get_or_create(master=model, language_code='fr',
                                              defaults=defaults)



def unload_data(apps, schema_editor):
    Translation = apps.get_model('countries', 'CountryTranslation')
    Translation.objects.filter(language_code='en').delete()
    Translation.objects.filter(language_code='fr').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_auto_20161021_1206'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=unload_data),
    ]
