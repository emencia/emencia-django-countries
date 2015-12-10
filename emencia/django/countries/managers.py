"""Managers for emencia.django.countries"""
from django.db import models

class CountryManager(models.Manager):
    """Manager for the countries"""
    
    def leveled(self):
        """Return all countries with a level set"""
        
        # Compatibility support for Django<1.6
        safe_get_queryset = (self.get_query_set if hasattr(self, 'get_query_set') else self.get_queryset)
        
        return safe_get_queryset.exclude(level=0)
    

                        
