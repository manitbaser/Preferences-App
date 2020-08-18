from rest_framework import serializers
from tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag','tag_id', 'articles']
        extra_kwargs = {'articles': {'required': False}}

class TagArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag','tag_id']