from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer