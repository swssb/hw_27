from rest_framework import serializers

from ads.models import Ad, Category, Selection
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


class AdUpdateSerializer(serializers.ModelSerializer):
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
        fields = ["name", "author", "price", "description", "category"]


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)
    owner = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Selection
        fields = "__all__"
