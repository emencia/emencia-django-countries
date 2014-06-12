"""Admin for emencia.django.countries"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.countries.models import Country


class CountryAdmin(admin.ModelAdmin):
    search_fields = ('printable_name_en', 'name', 'iso', 'iso3')
    list_display = ('printable_name_en', 'name', 'iso', 'iso3', 'numcode','level')
    ordering = ('printable_name_en',)
    fieldsets = ((None, {'fields': ('printable_name_en','printable_name_fr', 'name')}),
                 (_('References'), {'fields': ('iso', 'iso3', 'numcode')}),
                 (None, {'fields': ('level',)}),)
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Country, CountryAdmin)
