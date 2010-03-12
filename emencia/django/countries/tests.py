"""Unit tests for emencia.django.countries"""
from django.test import TestCase

from django.template import Context, Template
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

    def test_templatetags(self):
        t = Template("""
        {% load countries_tags %}
        {% get_countries %}
        {{ COUNTRIES|length }}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(), '244')

        t = Template("""
        {% load countries_tags %}
        {% get_countries as MY_COUNTRIES %}
        {{ MY_COUNTRIES|length }}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(), '244')

        t = Template("""
        {% load countries_tags %}
        {% get_countries_leveled %}
        {{ COUNTRIES|length }}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(), '0')

        france = Country.objects.get(iso='FR')
        france.level = 100
        france.save()

        t = Template("""
        {% load countries_tags %}
        {% get_countries_leveled as MY_COUNTRIES %}
        {{ MY_COUNTRIES|length }}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(), '1')
