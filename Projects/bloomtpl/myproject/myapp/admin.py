from django.contrib import admin
from .models import BankDetails, Product
from .models import Category
from .models import BuyerProfile
from .models import SellerProfile
from .models import Address
from .models import BankDetails

# Register your models here.
admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
admin.site.register(Address)
admin.site.register(BankDetails)