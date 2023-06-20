from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=10, unique=True, null=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
