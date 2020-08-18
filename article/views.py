from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer
from tag.models import Tag
from tag.serializers import TagSerializer
from tag.models import Tag
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import user_passes_test
from rest_framework import status
from itertools import chain

class ArticleViewSet(viewsets.ModelViewSet):
    """
    Returns all the articles and their details using given JWT token.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, pk=None):
        if request.user.is_superuser:
            tag = Tag.objects.filter(tag_id=pk)
            articleset = set()
            for t in tag:
                articleset = set(chain(articleset,TagSerializer(t).data["articles"]))
            articles = ArticleSerializer(Article.objects.filter(article_id__in= articleset),many=True).data
            return Response(ArticleSerializer(articles, many=True).data)


        else:
            res = {'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)


    # @action(detail=True)
    # def tag(self,request,pk):
    #     """
    #     Returns the tag and its details along with the mapped articles.
    #     """
    #     if request.user.is_superuser:
    #         tag = Tag.objects.filter(tag_id=pk)
    #         return Response(TagSerializer(tag, many=True).data)
    #     else:
    #         res = {'error': 'can not authenticate with the given credentials or the account has been deactivated'}
    #         return Response(res, status=status.HTTP_403_FORBIDDEN)
