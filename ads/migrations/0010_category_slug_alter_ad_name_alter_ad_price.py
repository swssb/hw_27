# Generated by Django 4.2.2 on 2023-06-21 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0009_selection"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                max_length=10,
                null=True,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[django.core.validators.MinLengthValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="price",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]