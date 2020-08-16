from rest_framework import serializers
from.models import User
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model = User
        fields = ['email', 'username', 'first_name', 'last_name',
                  'created_at', 'password','user_id']
        extra_kwargs = {'password': {'write_only': True}}
        

class UserPreferencesSerializer(serializers.ModelSerializer):
        
    class Meta(object):
        model = User
        fields = ['preferences']


class UserDeactivateSerializer(serializers.ModelSerializer):
        
    class Meta(object):
        model = User
        fields = ['is_active']