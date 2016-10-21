# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations



def forwards_func(apps, schema_editor):
    MyModel = apps.get_model('countries', 'Country')
    MyModelTranslation = apps.get_model('countries', 'CountryTranslation')

    for object in MyModel.objects.all():
        MyModelTranslation.objects.create(
            master_id=object.pk,
            language_code='en',
            name=object.name,
            printable_name=object.printable_name,
        )

def backwards_func(apps, schema_editor):
    MyModel = apps.get_model('countries', 'Country')
    MyModelTranslation = apps.get_model('countries', 'CountryTranslation')

    for object in MyModel.objects.all():
        translation = MyModelTranslation.objects.get(master_id=object.pk,
                                                     language_code='en')
        object.name = translation.name
        object.printable_name = translation.printable_name
        object.save()   # Note this only calls Model.save() in South.


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20161021_1144'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
