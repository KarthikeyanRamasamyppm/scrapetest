from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name