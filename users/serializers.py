from rest_framework import serializers

from users.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
