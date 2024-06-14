# products/urls.py

from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Buyer URLs
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Seller URLs
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('read/', views.ProductReadAllView.as_view(), name='product-read-all'),
    path('read/<int:pk>/', views.ProductReadDetailView.as_view(), name='product-read-detail'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('', include(router.urls)),

]