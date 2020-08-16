from rest_framework import serializers
from article.models import Article
# from tag.serializers import TagSerializer

class ArticleSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        # fields = ['author','title', 'article_id', 'publish_date']
        fields = ['author','title', 'article_id']
        # fields = ['author','title', 'article_id', 'publish_date', 'tags']
        # extra_kwargs = {'tags': {'required': False}}