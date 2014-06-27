"""Admin for emencia.django.countries"""
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf import settings

from emencia.django.countries.models import Country

fields = ['printable_name_%s' % lang[0] for lang in settings.LANGUAGES ]

class CountryAdmin(admin.ModelAdmin):
    search_fields = fields + ['name', 'iso', 'iso3']
    list_display = fields + ['name', 'iso', 'iso3', 'numcode','level']
    ordering = ('printable_name_en',)
    fieldsets = ((None, {'fields': fields + ['name']}),
                 (_('References'), {'fields': ('iso', 'iso3', 'numcode')}),
                 (None, {'fields': ('level',)}),)
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Country, CountryAdmin)
