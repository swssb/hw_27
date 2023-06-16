from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    ADMIN = "admin"
    MODERATOR = "moderator"
    ROLES = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Администратор"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLES, default='member')
    age = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
