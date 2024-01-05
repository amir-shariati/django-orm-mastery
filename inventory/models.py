from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
