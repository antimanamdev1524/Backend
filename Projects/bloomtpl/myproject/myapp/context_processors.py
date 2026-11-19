from .models import Category
from .models import BuyerProfile
from .models import SellerProfile

def categories(request):
    categories = Category.objects.filter(parent= None)
    return {'categories': categories}

def profile(request):
    if request.user.is_authenticated:
        try:
            buyer_profile = BuyerProfile.objects.get(user=request.user)
            return {'profile': buyer_profile}
        except BuyerProfile.DoesNotExist:
            try:
                seller_profile = SellerProfile.objects.get(user=request.user)
                return {'profile':seller_profile}
            except SellerProfile.DoesNotExist:
                return {'profile': None}
    return {'profile': None}
