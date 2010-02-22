"""Unit tests for emencia.django.countries"""
from django.test import TestCase

from emencia.django.countries.models import Country


class CountryTestCase(TestCase):
    """Tests for Country model"""

    def test_manager(self):
        countries = Country.objects.all()
        self.assertEquals(countries.count(), 244)
        self.assertEquals(countries[0], Country.objects.get(iso='AF'))

        countries = Country.objects.leveled()
        self.assertEquals(countries.count(), 0)

        france = Country.objects.get(iso='FR')
        france.level = 100
        france.save()

        countries = Country.objects.leveled()
        self.assertEquals(countries.count(), 1)

        countries = Country.objects.all()
        self.assertEquals(countries.count(), 244)
        self.assertEquals(countries[0], france)
