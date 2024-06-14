from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.userprofile.user_type == 'admin'

class IsBuyerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.userprofile.user_type == 'buyer'

class IsSellerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.userprofile.user_type == 'seller'
