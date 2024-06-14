#orders/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from sellers.models import SellerProfile

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"