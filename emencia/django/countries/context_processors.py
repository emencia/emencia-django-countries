"""Context Processors for emencia.django.countries"""
from emencia.django.countries.models import Country

def countries(request):
    """Add the countries to the list"""
    return {'COUNTRIES_LIST': Country.objects.all(),
            'COUNTRIES_LIST_LEVELED': Country.objects.leveled()}


