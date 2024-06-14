from django.urls import path
from .views import AdminDashboardView, ManageUsersView, ManageSellersView, ManageBuyersView, ManageProductsView, ManageOrdersView

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('users/', ManageUsersView.as_view(), name='manage-users'),
    path('sellers/', ManageSellersView.as_view(), name='manage-sellers'),
    path('buyers/', ManageBuyersView.as_view(), name='manage-buyers'),
    path('products/', ManageProductsView.as_view(), name='manage-products'),
    path('orders/', ManageOrdersView.as_view(), name='manage-orders'),
]
