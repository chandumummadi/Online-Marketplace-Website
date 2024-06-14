#users/urls.py

from django.urls import path
from .views import BuyerRegisterView, SellerRegisterView, LoginView


urlpatterns = [
    path('register/buyer/', BuyerRegisterView.as_view(), name='register-buyer'),
    path('register/seller/', SellerRegisterView.as_view(), name='register-seller'),
    path('login/', LoginView.as_view(), name='login'),

]
