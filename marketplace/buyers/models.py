from django.db import models
from users.models import UserProfile

class BuyersProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile.user.username

class DeliveryAddress(models.Model):
    buyer_profile = models.ForeignKey(BuyersProfile, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()

    def __str__(self):
        return self.address

class CardDetail(models.Model):
    buyer_profile = models.ForeignKey(BuyersProfile, on_delete=models.CASCADE, related_name='cards')
    cardholder_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3, default='000')

    def __str__(self):
        return f"**** **** **** {self.card_number[-4:]}"
