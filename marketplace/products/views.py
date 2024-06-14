# products/views.py

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from sellers.models import SellerProfile
from .models import Product
import json
from rest_framework import viewsets
from .serializers import ProductSerializer

# Buyer Views
class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)

class ProductDetailView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock,
                'created_at': product.created_at,
                'updated_at': product.updated_at
            })
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)



# Seller Views
class ProductCreateView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        try:
            seller_profile = SellerProfile.objects.get(pk=data['seller_profile'])
            product = Product.objects.create(
                name=data['name'],
                description=data['description'],
                price=data['price'],
                stock=data['stock'],
                seller_profile=seller_profile  # Ensure the seller_profile is correctly set
            )
            return JsonResponse({"message": "Product created successfully"}, status=201)
        except SellerProfile.DoesNotExist:
            return JsonResponse({"error": "Seller profile not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

class ProductUpdateView(View):
    @csrf_exempt
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            data = json.loads(request.body)
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = data.get('price', product.price)
            product.stock = data.get('stock', product.stock)
            product.save()
            return JsonResponse({"message": "Product updated successfully"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

class ProductReadAllView(View):
    def get(self, request):
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)

class ProductReadDetailView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock,
                'created_at': product.created_at,
                'updated_at': product.updated_at
            })
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

class ProductDeleteView(View):
    @csrf_exempt
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return JsonResponse({"message": "Product deleted successfully"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer