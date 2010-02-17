"""Managers for emencia.django.directory"""
from django.db import models

class CountryManager(models.Manager):
    """Manager for the countries"""
    
    def leveled(self):
        """Return all countries with a level set"""
        return self.get_query_set().exclude(level=0)
    

                        
