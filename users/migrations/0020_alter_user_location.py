# Generated by Django 4.2.2 on 2023-06-22 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0019_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.location",
            ),
        ),
    ]
