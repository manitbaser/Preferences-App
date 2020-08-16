from django.urls import path, include
from rest_framework.routers import DefaultRouter
from preferences import views

router = DefaultRouter()
router.register(r'', views.PreferencesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]