#users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class BuyerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        UserProfile.objects.create(
            user=user,
            user_type='buyer',
            phone_number=self.cleaned_data['phone_number']
        )
        return user

class SellerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        UserProfile.objects.create(
            user=user,
            user_type='seller',
            phone_number=self.cleaned_data['phone_number']
        )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
