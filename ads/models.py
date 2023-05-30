from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=20)

class Ad(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=40)
    is_published = models.BooleanField()