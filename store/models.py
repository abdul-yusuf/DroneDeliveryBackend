from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    vendor = models.CharField(max_length=40, blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=5, choices=(('grams', 'Grams'), ('kg', 'KiloGrams'),))

    def __str__(self):
        return f"{self.name} "


class Category(models.Model):
    name = models.CharField(max_length=20)

