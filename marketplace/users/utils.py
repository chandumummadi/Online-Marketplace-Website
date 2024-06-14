#users/utils.py

from django.contrib.auth.models import User
from users.models import UserProfile
from sellers.models import SellerProfile
from buyers.models import BuyerProfile

def get_user_profile(user: User) -> dict:
    try:
        user_profile = UserProfile.objects.get(user=user)
        profile_data = {
            "username": user.username,
            "email": user.email,
            "user_type": user_profile.user_type,
        }

        if user_profile.user_type == 'seller':
            seller_profile = SellerProfile.objects.get(user_profile=user_profile)
            profile_data.update({
                "store_name": seller_profile.store_name,
                "store_address": seller_profile.store_address,
                "contact_details": seller_profile.contact_details,
            })
        elif user_profile.user_type == 'buyer':
            buyer_profile = BuyerProfile.objects.get(user_profile=user_profile)
            profile_data.update({
                "delivery_addresses": list(buyer_profile.addresses.values()),
                "card_details": list(buyer_profile.cards.values()),
            })
        
        return profile_data
    except UserProfile.DoesNotExist:
        return {"error": "User profile not found"}
    except SellerProfile.DoesNotExist:
        return {"error": "Seller profile not found"}
    except BuyerProfile.DoesNotExist:
        return {"error": "Buyer profile not found"}
