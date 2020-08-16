from django.db import models
from article.models import Article

class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=True)
    tag_id = models.AutoField(primary_key=True)
    articles = models.ManyToManyField(Article, related_name='tags', blank=True)
    
    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag_id']
        