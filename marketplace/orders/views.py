#orders/views.py

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Order
from sellers.models import SellerProfile
from buyers.models import BuyersProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class OrderListView(View):
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
    def get(self, request, pk):
        try:
            seller_profile = SellerProfile.objects.get(user_profile__user=request.user)
            order = Order.objects.get(pk=pk, seller=seller_profile)
            data = {
                "id": order.id,
                "buyer": order.buyer.user.username,
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
class BuyerOrderListView(View):
    def get(self, request):
        try:
            buyer_profile = BuyersProfile.objects.get(user=request.user)
            orders = Order.objects.filter(buyer=buyer_profile)
            data = list(orders.values())
            return JsonResponse(data, safe=False)
        except BuyersProfile.DoesNotExist:
            return JsonResponse({"error": "Buyer profile not found"}, status=404)

@method_decorator(login_required, name='dispatch')
class BuyerOrderDetailView(View):
    def get(self, request, pk):
        try:
            buyer_profile = BuyersProfile.objects.get(user=request.user)
            order = Order.objects.get(pk=pk, buyer=buyer_profile)
            data = {
                "id": order.id,
                "seller": order.seller.user_profile.user.username,
                "product": order.product.name,
                "quantity": order.quantity,
                "status": order.status,
                "created_at": order.created_at,
                "updated_at": order.updated_at
            }
            return JsonResponse(data, safe=False)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
        except BuyersProfile.DoesNotExist:
            return JsonResponse({"error": "Buyer profile not found"}, status=404)
