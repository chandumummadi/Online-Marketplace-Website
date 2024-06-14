from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsBuyerUser
from .models import BuyersProfile, DeliveryAddress, CardDetail
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class BuyersDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get(self, request):
        buyer_profile = BuyersProfile.objects.get(user_profile__user=request.user)
        addresses = list(buyer_profile.addresses.values())
        cards = list(buyer_profile.cards.values())
        data = {
            "addresses": addresses,
            "cards": cards,
            "order_history_url": "/buyers/orders/",
            "add_address_url": "/buyers/addresses/add/",
            "add_card_url": "/buyers/cards/add/",
        }
        return Response(data)

@method_decorator(login_required, name='dispatch')
class AddAddressView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def post(self, request):
        buyer_profile = BuyersProfile.objects.get(user_profile__user=request.user)
        address = DeliveryAddress.objects.create(
            buyer_profile=buyer_profile,
            address=request.data['address']
        )
        return Response({"message": "Address added successfully"})

@method_decorator(login_required, name='dispatch')
class AddCardView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def post(self, request):
        buyer_profile = BuyersProfile.objects.get(user_profile__user=request.user)
        card = CardDetail.objects.create(
            buyer_profile=buyer_profile,
            cardholder_name=request.data['cardholder_name'],
            card_number=request.data['card_number'],
            expiry_date=request.data['expiry_date'],
            cvv=request.data['cvv']
        )
        return Response({"message": "Card added successfully"})

@method_decorator(login_required, name='dispatch')
class BuyersOrderHistoryView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get(self, request):
        orders = Order.objects.filter(buyer=request.user)
        return Response(list(orders.values()))

@method_decorator(login_required, name='dispatch')
class BuyersOrderDetailView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get(self, request, pk):
        order = Order.objects.get(pk=pk, buyer=request.user)
        data = {
            "id": order.id,
            "product": order.product.name,
            "quantity": order.quantity,
            "status": order.status,
            "created_at": order.created_at,
            "updated_at": order.updated_at
        }
        return Response(data)
