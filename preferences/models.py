from django.db import models
from tag.models import Tag

class Preferences(models.Model):
    preference = models.CharField(max_length=50, blank=True, unique=True)
    preference_id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(Tag, related_name='preferences', blank=True)
    
    class Meta:
        ordering = ['preference']
    
    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.preference