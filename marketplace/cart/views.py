from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsBuyerUser
from .models import CartItem
from products.models import Product

@method_decorator(login_required, name='dispatch')
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return Response({"message": "Product added to cart"}, status=201)

@method_decorator(login_required, name='dispatch')
class CartView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        cart_data = [{"product": item.product.name, "quantity": item.quantity, "price": item.product.price} for item in cart_items]
        return Response(cart_data)
