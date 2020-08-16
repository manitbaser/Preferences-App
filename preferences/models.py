from django.db import models
from tag.models import Tag

class Preferences(models.Model):
    preference = models.CharField(max_length=50, blank=True, unique=True)
    preference_id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(Tag, related_name='preferences', blank=True)
    
    class Meta:
        ordering = ['preference']
    
    def __str__(self):
        return self.preference