from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer
from tag.models import Tag
from tag.serializers import TagSerializer
from tag.models import Tag
from rest_framework.decorators import action
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):
    """
    Returns all the articles and their details using given JWT token.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @action(detail=True)
    def tag(self,request,pk):
        """
        Returns the tag and its details along with the mapped articles.
        """
        tag = Tag.objects.filter(tag_id=pk)
        return Response(TagSerializer(tag, many=True).data)
