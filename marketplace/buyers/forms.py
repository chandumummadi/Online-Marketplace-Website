from django import forms
from django.contrib.auth.models import User
from .models import BuyerProfile, DeliveryAddress, CardDetail

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ['address']

class CardDetailForm(forms.ModelForm):
    class Meta:
        model = CardDetail
        fields = ['card_number', 'expiry_date', 'cardholder_name']