#orders/urls.py

from django.urls import path
from .views import OrderListView, OrderDetailView, BuyerOrderListView, BuyerOrderDetailView

urlpatterns = [
    path('seller/orders/', OrderListView.as_view(), name='seller-order-list'),
    path('seller/orders/<int:pk>/', OrderDetailView.as_view(), name='seller-order-detail'),
    path('buyer/orders/', BuyerOrderListView.as_view(), name='buyer-order-list'),
    path('buyer/orders/<int:pk>/', BuyerOrderDetailView.as_view(), name='buyer-order-detail'),
]
