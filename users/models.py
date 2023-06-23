from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

USER_MIN_AGE = 9
EMAIL_DOMAINS = ["rambler.ru"]


def birth_validation(value):
    difference = relativedelta(date.today(), value).years
    if difference < USER_MIN_AGE:
        raise ValidationError(f"User age must be older than {USER_MIN_AGE}")


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
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(validators=[birth_validation])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
