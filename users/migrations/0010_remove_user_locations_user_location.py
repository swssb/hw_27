# Generated by Django 4.2.1 on 2023-06-09 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_rename_location_user_locations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="locations",
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.location",
            ),
            preserve_default=False,
        ),
    ]
