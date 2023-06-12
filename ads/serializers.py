from rest_framework import serializers

from ads.models import Ad, Category
from users.models import User


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Ad
        fields = '__all__'
