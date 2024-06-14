from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAdminUser
from users.models import UserProfile
from buyers.models import BuyersProfile, DeliveryAddress, CardDetail
from sellers.models import SellerProfile
from products.models import Product
from orders.models import Order

class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Admin Dashboard"})

class ManageUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = UserProfile.objects.values()
        return Response(users)

class ManageSellersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        sellers = SellerProfile.objects.values()
        return Response(sellers)

class ManageBuyersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        buyers = BuyersProfile.objects.values()
        return Response(buyers)

class ManageProductsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        products = Product.objects.values()
        return Response(products)

class ManageOrdersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.values()
        return Response(orders)
