# Generated by Django 4.2.2 on 2023-06-21 15:37

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_alter_user_birth_date_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(validators=[users.models.birth_validation]),
        ),
    ]
