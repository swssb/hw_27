# Generated by Django 4.2.2 on 2023-06-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0010_category_slug_alter_ad_name_alter_ad_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="description",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]