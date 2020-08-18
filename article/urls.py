from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views
from article.views import ArticleViewSet

router = DefaultRouter()
router.register(r'', views.ArticleViewSet)

tag = ArticleViewSet.as_view({
    'get': 'tag'
})

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/tag/',tag)
]