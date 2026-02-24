from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    specifications = models.JSONField()
    rating = models.CharField(max_length=500, null=True, blank=True)
    review_count = models.CharField(max_length=500, null=True, blank=True)
    amazon_url = models.CharField(max_length=500, null=True, blank=True)
    availability = models.CharField(max_length=500, null=True, blank=True)
    market_analysis = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name