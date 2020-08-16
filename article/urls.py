from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views

router = DefaultRouter()
router.register(r'', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]