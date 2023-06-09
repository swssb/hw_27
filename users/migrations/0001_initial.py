# Generated by Django 4.2.1 on 2023-06-05 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ("lng", models.DecimalField(decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=50)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("member", "Пользователь"),
                            ("moderator", "Модератор"),
                            ("admin", "Администратор"),
                        ],
                        default="member",
                        max_length=30,
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.location"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
