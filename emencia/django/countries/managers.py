"""Managers for emencia.django.countries"""
from parler.managers import TranslatableManager

class CountryManager(TranslatableManager):
    """Manager for the countries"""

    def leveled(self):
        """Return all countries with a level set"""

        get_queryset = getattr(self, 'get_queryset', None)

        # Compatibility support for Django<1.6
        if get_queryset is None:
            get_queryset = self.get_query_set

        return get_queryset.exclude(level=0)
