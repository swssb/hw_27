# factories.py

import factory

from ads.models import Ad, Category, Selection
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('ean', length=8)
    birth_date = "2000-03-12"
    email = factory.Faker('ean', length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Продам гараж!"
    author = factory.SubFactory(UserFactory)
    price = 50
    description = "Хороший теплый с замком"

class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection
    name = "My selection"
    owner = factory.SubFactory(UserFactory)