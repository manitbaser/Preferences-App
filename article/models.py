from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=80, blank=True)
    article_id = models.AutoField(primary_key=True)
    publish_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']