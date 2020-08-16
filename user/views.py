import jwt
from rest_framework_jwt.serializers import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, UserPreferencesSerializer, UserDeactivateSerializer
from .models import User
from preference import settings
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin
from preferences.serializers import PreferencesMapping
from preferences.models import Preferences
from tag.models import Tag
from tag.serializers import TagSerializer
from article.models import Article
from article.serializers import ArticleSerializer

class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=request.data['email'], password=request.data['password'])
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        user_details = {}
        user_details['name'] = "%s %s" % (user.first_name, user.last_name)
        user_details['token'] = token
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(user_details, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)


class UserInfoView(RetrieveUpdateAPIView, UpdateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('username', {})
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserPreferencesView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPreferencesSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('username', {})
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeactivate(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDeactivateSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = request.data.get('username', {})
        request.user.is_active = False
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("The user has been deactivated", status=status.HTTP_200_OK)


class UserArticlesView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        preferences = set()
        serializer_class = UserPreferencesSerializer
        serializer = serializer_class(request.user)
        for pref in serializer.data["preferences"]:
            preferences.add(pref)
        # return Response(preferences, status=status.HTTP_200_OK)
        tags = set()
        for preference in Preferences.objects.all():
            serializer = PreferencesMapping(preference)
            if serializer.data["preference_id"] in preferences:
                for tag in serializer.data["tags"]:
                    tags.add(tag)
        # return Response(tags, status=status.HTTP_200_OK)
        articles = set()
        for tag in Tag.objects.all():
            serializer = TagSerializer(tag)
            if serializer.data["tag_id"] in tags:
                for article in serializer.data["articles"]:
                    articles.add(article)
        # return Response(articles, status=status.HTTP_200_OK)
        Articles = list()
        for article in articles:
            Articles.append(ArticleSerializer(Article.objects.get(article_id  = article)).data)
        return Response(Articles, status=status.HTTP_200_OK)