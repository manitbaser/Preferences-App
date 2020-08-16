from rest_framework import serializers
from preferences.models import Preferences
class PreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ['preference','preference_id']

class PreferencesMapping(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ['preference_id','tags']