# Generated by Django 4.2.1 on 2023-06-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0005_alter_ad_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
