from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer
from tag.models import Tag
from tag.serializers import TagSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns all the articles and their details using given JWT token.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    # def show_tags(self, instance):
        # queryset = Tag.objects.all()
        # serializer = tag
        # serializer_class
