#sellers/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import SellerProfile
from .forms import SellerProfileUpdateForm
from products.models import Product
from orders.models import Order
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsSellerUser
import json

@method_decorator(login_required, name='dispatch')
class SellerDashboardView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]

    def get(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            products = Product.objects.filter(seller_profile=seller_profile)
            orders = Order.objects.filter(seller=seller_profile)
            net_revenue = sum(order.product.price * order.quantity for order in orders)

            data = {
                "net_revenue": net_revenue,
                "add_more_items_url": "/products/create/",
                "manage_items_url": "/products/",
            }
            return JsonResponse(data, safe=False)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class SellerProfileDetailView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]
    def get(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            products = Product.objects.filter(seller_profile=seller_profile)
            data = {
                "store_name": seller_profile.store_name,
                "store_address": seller_profile.store_address,
                "products": list(products.values()),
                "contact_details": seller_profile.contact_details,
                "ssn": seller_profile.ssn,
                "bank_details": seller_profile.bank_details
            }
            return JsonResponse(data, safe=False)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class SellerProfileUpdateView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]
    def get(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            form = SellerProfileUpdateForm(instance=seller_profile)
            return JsonResponse(form.data, safe=False)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

    def post(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            data = json.loads(request.body)
            form = SellerProfileUpdateForm(data, instance=seller_profile)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Profile updated successfully"}, status=200)
            return JsonResponse(form.errors, status=400)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class OrderListView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]
    def get(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            orders = Order.objects.filter(seller=seller_profile)
            data = list(orders.values())
            return JsonResponse(data, safe=False)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class OrderDetailView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]
    
    def get(self, request, pk):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            order = Order.objects.get(pk=pk, seller=seller_profile)
            data = {
                "id": order.id,
                "buyer": order.buyer.username,
                "product": order.product.name,
                "quantity": order.quantity,
                "status": order.status,
                "created_at": order.created_at,
                "updated_at": order.updated_at
            }
            return JsonResponse(data, safe=False)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class SellerProductListView(View):
    permission_classes = [IsAuthenticated, IsSellerUser]
    def get(self, request):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            products = Product.objects.filter(seller_profile=seller_profile)
            data = list(products.values())
            return JsonResponse(data, safe=False)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)