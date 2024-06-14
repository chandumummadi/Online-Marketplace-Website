# products/models.py

from django.db import models
from sellers.models import SellerProfile

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller_profile = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)  # Make this non-nullable

    def __str__(self):
        return self.name
