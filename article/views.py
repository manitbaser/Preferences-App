from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns all the articles and their details using given JWT token.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer