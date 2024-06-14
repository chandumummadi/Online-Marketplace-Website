#sellers/models.py

from django.db import models
from users.models import UserProfile

class SellerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    store_address = models.TextField()
    contact_details = models.TextField()
    ssn = models.CharField(max_length=11)
    bank_details = models.TextField()

    def __str__(self):
        return self.user_profile.user.username
