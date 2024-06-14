#sellers/urls.py

from django.urls import path
from .views import SellerDashboardView, SellerProfileDetailView, SellerProfileUpdateView, OrderListView, OrderDetailView, SellerProductListView

urlpatterns = [
    path('dashboard/', SellerDashboardView.as_view(), name='seller-dashboard'),
    path('profile/', SellerProfileDetailView.as_view(), name='seller-profile-detail'),
    path('profile/update/', SellerProfileUpdateView.as_view(), name='seller-profile-update'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('products/', SellerProductListView.as_view(), name='seller-product-list'),
]
