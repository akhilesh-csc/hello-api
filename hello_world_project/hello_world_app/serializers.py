# hello_world_app/serializers.py
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        # Use the UserProfile model for serialization
        model = UserProfile
        # Specify the fields to include in the serialized data
        fields = ['latitude', 'longitude']
