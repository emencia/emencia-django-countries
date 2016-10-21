"""Admin for emencia.django.countries"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from parler.admin import TranslatableAdmin

from emencia.django.countries.models import Country


class CountryAdmin(TranslatableAdmin):
    list_display = ('printable_name', 'name', 'iso', 'iso3', 'numcode','level')
    search_fields = (
        'translations__printable_name', 'translations__name', 'iso', 'iso3')

    fieldsets = ((None, {'fields': ('printable_name', 'name')}),
                 (_('References'), {'fields': ('iso', 'iso3', 'numcode')}),
                 (None, {'fields': ('level',)}),)
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Country, CountryAdmin)

