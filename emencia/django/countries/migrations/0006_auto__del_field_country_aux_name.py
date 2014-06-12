# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Country.aux_name'
        db.delete_column('country', 'aux_name')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Country.aux_name'
        raise RuntimeError("Cannot reverse this migration. 'Country.aux_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Country.aux_name'
        db.add_column('country', 'aux_name',
                      self.gf('django.db.models.fields.CharField')(max_length=128),
                      keep_default=False)


    models = {
        u'countries.country': {
            'Meta': {'ordering': "('-level',)", 'object_name': 'Country', 'db_table': "'country'"},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'printable_name_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'printable_name_fr': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['countries']