"""Templatetags for emencia.django.countries"""
from django.template import Node
from django.template import Library
from django.template import TemplateSyntaxError

from emencia.django.countries.models import Country

register = Library()

class ContextSetterNode(Node):
    """Node for settings data in the context"""
    def __init__(self, varname, value):
        self.varname, self.value = varname, value

    def render(self, context):
        context[self.varname] = self.value
        return ''

@register.tag
def get_countries(parser, token):
    bits = token.split_contents()
    
    if len(bits) not in [1, 3]:
        raise TemplateSyntaxError, "Invalid syntax for get_countries tag : {% get_countries [as COUNTRIES] %}"

    varname = 'COUNTRIES'
    if len(bits) == 3:
        if bits[1] != 'as':
            raise TemplateSyntaxError, "first argument for get_countries tag must be 'as'"
        varname = bits[2]
    
    return ContextSetterNode(varname, Country.objects.all())

@register.tag
def get_countries_leveled(parser, token):
    bits = token.split_contents()
    
    if len(bits) not in [1, 3]:
        raise TemplateSyntaxError, "Invalid syntax for get_countries_leveled tag : {% get_countries_leveled [as COUNTRIES] %}"

    varname = 'COUNTRIES'
    if len(bits) == 3:
        if bits[1] != 'as':
            raise TemplateSyntaxError, "first argument for get_countries_leveled tag must be 'as'"
        varname = bits[2]
    
    return ContextSetterNode(varname, Country.objects.leveled())

