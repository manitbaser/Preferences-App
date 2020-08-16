from django.urls import path

from .views import RegisterUserAPIView, UserInfoView, UserPreferencesView, UserDeactivate, GetToken, UserArticlesView
app_name = 'user'
urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()), # Create new user and obtain token
    path('token/', GetToken), # Obtain token
    path('info/', UserInfoView.as_view()), # View and update user info
    path('preferences/', UserPreferencesView.as_view()), # View and edit user preferences
    path('deactivate/', UserDeactivate.as_view()), # Deactivate user
    path('suggestions/', UserArticlesView.as_view()) # Get suggestions
]