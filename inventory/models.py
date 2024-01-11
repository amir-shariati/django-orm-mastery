from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product name')
    qty = models.IntegerField(verbose_name='Product quantity')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
