"""Models for emencia.django.countries"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields

from emencia.django.countries.managers import CountryManager


class Country(TranslatableModel):
    """Country model based on django-countries"""
    iso = models.CharField(_('ISO alpha-2'), max_length=2, primary_key=True)
    iso3 = models.CharField(_('ISO alpha-3'), max_length=3, null=True)
    numcode = models.PositiveSmallIntegerField(_('ISO numeric'), null=True)
    level = models.PositiveSmallIntegerField(_('level'), default=0)

    translations = TranslatedFields(
        name = models.CharField(_('Official name (CAPS)'), max_length=128),
        printable_name = models.CharField(_('Country name'), max_length=128),
    )

    objects = CountryManager()

    def __unicode__(self):
        return self.printable_name

    class Meta:
        db_table = 'country'
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('-level', 'iso3')
