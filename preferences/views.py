from rest_framework import viewsets
from preferences.models import Preferences
from preferences.serializers import PreferencesSerializer

class PreferencesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Preferences.objects.all()
    serializer_class = PreferencesSerializer