from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['author','title', 'article_id', 'publish_date']
        fields = ['author','title', 'article_id']