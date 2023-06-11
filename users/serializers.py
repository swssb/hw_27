from rest_framework import serializers

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'