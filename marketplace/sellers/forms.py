#sellers/forms.py

from django import forms
from .models import SellerProfile

class SellerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['store_name', 'store_address', 'contact_details', 'ssn', 'bank_details']
