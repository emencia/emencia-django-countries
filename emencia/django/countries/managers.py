"""Managers for emencia.django.countries"""
from django.db import models

class CountryManager(models.Manager):
    """Manager for the countries"""
    
    def leveled(self):
        """Return all countries with a level set"""
        return self.get_query_set().exclude(level=0)
    

                        
