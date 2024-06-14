#users/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import BuyerRegistrationForm, SellerRegistrationForm, LoginForm
from django.http import JsonResponse
from sellers.models import SellerProfile
from rest_framework.authtoken.models import Token
from .models import UserProfile
import json

class BuyerRegisterView(View):
    def post(self, request):
        data = json.loads(request.body)
        form = BuyerRegistrationForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Buyer registered successfully"}, status=201)
        return JsonResponse(form.errors, status=400)

class SellerRegisterView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password1']
        phone_number = data['phone_number']

        if data['password1'] != data['password2']:
            return JsonResponse({"error": "Passwords do not match"}, status=400)

        try:
            form = SellerRegistrationForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Seller registered successfully"}, status=201)
            return JsonResponse(form.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        form = LoginForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                user_profile = UserProfile.objects.get(user=user)
                # Get or create token for the user
                token, created = Token.objects.get_or_create(user=user)
                if user_profile.user_type == 'buyer':
                    return JsonResponse({
                        "message": "Logged in successfully",
                        "redirect_url": "/buyers/dashboard/",
                        "token": token.key
                    }, status=200)
                elif user_profile.user_type == 'seller':
                    return JsonResponse({
                        "message": "Logged in successfully",
                        "redirect_url": "/sellers/dashboard/",
                        "token": token.key
                    }, status=200)
                else:
                    return JsonResponse({"message": "User type not recognized"}, status=400)
            except UserProfile.DoesNotExist:
                return JsonResponse({"message": "User profile not found"}, status=400)
        return JsonResponse(form.errors, status=400)
