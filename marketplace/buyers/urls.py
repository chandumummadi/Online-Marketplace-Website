from django.urls import path
from .views import BuyersDashboardView, AddAddressView, AddCardView, BuyersOrderHistoryView, BuyersOrderDetailView

urlpatterns = [
    path('dashboard/', BuyersDashboardView.as_view(), name='buyers-dashboard'),
    path('addresses/add/', AddAddressView.as_view(), name='add-address'),
    path('cards/add/', AddCardView.as_view(), name='add-card'),
    path('orders/', BuyersOrderHistoryView.as_view(), name='buyers-order-history'),
    path('orders/<int:pk>/', BuyersOrderDetailView.as_view(), name='buyers-order-detail'),
]
