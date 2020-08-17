from django.urls import path

from .views import RegisterUserView, UserInfoView, UserPreferencesView, UserDeactivateView, GetTokenView, UserArticlesView
app_name = 'user'
urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', GetTokenView.as_view()),
    path('info/', UserInfoView.as_view()),
    path('preferences/', UserPreferencesView.as_view()),
    path('deactivate/', UserDeactivateView.as_view()),
    path('suggestions/', UserArticlesView.as_view())
]