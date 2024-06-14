from django.contrib import admin
from .models import BuyersProfile, DeliveryAddress, CardDetail

admin.site.register(BuyersProfile)
admin.site.register(DeliveryAddress)
admin.site.register(CardDetail)
